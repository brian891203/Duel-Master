<template>
  <div class="chat-container">
    <ChatSidebar :conversations="conversations" :currentConversation="currentConversation" @select="selectConversation"
      @new="createNewConversation" @delete="deleteConversation" />
    <div class="chat-main">
      <ChatHeader :title="currentConversation.title" @update:title="updateConversationTitle" />
      <ChatMessageList :messages="currentConversation.messages" />
      <ChatInput @send="handleMessageSend" @upload="handleFileUpload" />
    </div>
  </div>
  <Teleport to="body">
    <CardModal ref="cardModalRef" :card-info="cardInfo" :max-size="LARGE_CARD_BP.maxSize"
      :breakpoint-map="LARGE_CARD_BP.breakpointMap">
    </CardModal>
  </Teleport>
</template>

<script setup lang="ts">
import { useTemplateRef, watch } from 'vue'
import { questionAPI } from '../../api/question'
import { translateAPI } from '../../api/translation'
import { useConversation } from '../../composables/chat-room/useConversation'
import { LARGE_CARD_BP } from '../../config'
import YugiohCard from '../../example/yugioh'
import YugiohBackCard from '../../example/yugiohBack'
import {
  createCardMessage,
  createFileMessage,
  createSimpleMessage,
} from '../../utils/chat-room/createMessage'
import { sleep } from '../../utils/misc/methods'
import CardModal from '../modal/CardModal.vue'
import ChatHeader from './ChatHeader.vue'
import ChatInput from './ChatInput.vue'
import ChatMessageList from './ChatMessageList.vue'
import ChatSidebar from './Sidebar.vue'
import { dataAPI } from '../../api/data'
import { yCardtoFrontCardData } from '../../utils/ygoprodeck/transform'

// variables //
const cardInfo = { frontCardData: YugiohCard, backCardData: YugiohBackCard }

// template ref //
const cardModalRef = useTemplateRef('cardModalRef')

// composables //
const {
  conversations,
  currentConversation,
  createNewConversation,
  selectConversation,
  deleteConversation,
  updateConversationTitle,
} = useConversation()

// 問答模式 //
const questionMode = async (text: string) => {
  const { data } = await questionAPI(text)
  if (data.success) {
    const systemMessage = createSimpleMessage('System', data.answer)
    currentConversation.value.messages.push(systemMessage)
  }
}

// 翻譯模式 //
const translationMode = async (file: File, password: string) => {
  // promise
  const dataPromise = dataAPI(password)
  const translatePromise = translateAPI(file)

  // animation
  cardModalRef.value?.setResultObtained(false)
  await cardModalRef.value?.showModal()
  await sleep(500)
  await cardModalRef.value?.cardLeaving()

  // dataAPI
  const { data: cardData } = await dataPromise
  if ("data" in cardData) {
    cardModalRef.value?.setCardInfo({
      frontCardData: yCardtoFrontCardData(cardData.data[0])
    })
  } else {
    alert(`卡片資訊獲取失敗：${cardData.error}`)
  }

  // translateAPI
  const { data: translateData } = await translatePromise
  if (translateData.success) {
    cardModalRef.value?.setCardInfo({
      frontCardData: translateData.frontCardData
    })
    cardModalRef.value?.setResultObtained(true)
  } else {
    alert(`卡片翻譯失敗：${translateData.errMessage}`)
  }
  await cardModalRef.value?.cardEntering()
  if (translateData.success) {
    const card = cardModalRef.value?.getCardInfo()
    if (card) {
      const systemMessage = createCardMessage('System', card, '翻譯結果出爐辣🔥')
      currentConversation.value.messages.push(systemMessage)
    }
  }
}

// 處理上傳的訊息 //
const handleMessageSend = async (text: string) => {
  // Your message
  const userMessage = createSimpleMessage('You', text)
  currentConversation.value.messages.push(userMessage)

  // System message
  if (currentConversation.value.mode === 'question') {
    await sleep(500)
    questionMode(text)
  } else if (currentConversation.value.mode === 'translation') {
    if (text.match(/[0-9]{8}/)) {
      currentConversation.value.lastPassword = text
    }
  }
}

// 處理上傳的檔案 //
const handleFileUpload = async (file: File) => {
  // Your message
  const fileMessage = await createFileMessage('You', file, '可以幫我翻譯這張卡片嗎🥺？')
  currentConversation.value.messages.push(fileMessage)
  currentConversation.value.lastFile = file

  // System message
  currentConversation.value.mode = 'translation'
  await sleep(500)
  const systemMessage1 = createSimpleMessage('System', '好的，沒有問題🫡')
  currentConversation.value.messages.push(systemMessage1)
  await sleep(500)
  const systemMessage2 = createSimpleMessage('System', '請輸入密碼，我可以提供更多資訊🤫')
  currentConversation.value.messages.push(systemMessage2)
}

// 等待使用者輸入密碼，獲取密碼
watch(() => currentConversation.value.lastPassword, async (newPassword) => {
  if (newPassword) {
    await sleep(500)
    const systemMessage3 = createSimpleMessage('System', '翻譯中...')
    currentConversation.value.messages.push(systemMessage3)
    await sleep(500)
    if (currentConversation.value.lastFile) {
      translationMode(currentConversation.value.lastFile, newPassword)
    }
    currentConversation.value.lastPassword = ''
    currentConversation.value.lastFile = undefined
    currentConversation.value.mode = 'question'
  }
})
</script>

<style scoped lang="css">
.chat-container {
  position: relative;
  height: 100%;
  width: 100%;
}

.chat-main {
  position: relative;
  display: flex;
  flex-direction: column;
  height: 100%;
  margin: 0 auto;
  background-color: transparent;
  z-index: 1;
}
</style>
