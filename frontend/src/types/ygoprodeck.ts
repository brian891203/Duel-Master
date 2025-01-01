import type { CardType } from "yugioh-card"

export type ArrowTypeName = '' | 'Top' | 'Top-Right' | 'Right' | 'Bottom-Right' | 'Bottom' | 'Bottom-Left' | 'Left' | 'Top-Left'

export interface YCardSet {
  set_name: string
  set_code: string
  set_rarity: string
  set_rarity_code: string
  set_price: string
}

export interface YCardImage {
  id: number
  image_url: string
  image_url_small: string
  image_url_cropped: string
}

export interface YCardPrice {
  cardmarket_price: string
  tcgplayer_price: string
  ebay_price: string
  amazon_price: string
  coolstuffinc_price: string
}

export interface YLinkData {
  linkval: number // link 的數量
  linkmarkers: ArrowTypeName[] // * 對應 arrowList: ArrowType[] (註：但這裡是英文，如 ['Top', 'Bottom-Left'])
}

export interface YCard {
  id: string // * 對應 password: string
  name: string // * 對應 name: string
  type: string // * 對應 type: Type (註：這裡原本是類似 'Effect Monster' 這樣的寫法，所以要抓單字並改小寫)
  frameType: CardType // * 對應 cardType: CardType
  desc: string // * 對應 description: string
  ygoprodeck_url: string // X
  atk?: number // * 對應 atk: number
  def?: number // * 對應 def: number
  level?: number // * 對應 level: number
  race?: string // * 對應 monsterType: string (註：但這裡是英文)
  attribute?: string // * 對應 attribute: Attribute (註：全大寫)
  archetype?: string // X
  scale?: number // * 對應 pendulumScale: number
  pend_desc?: string // * 對應 pendulumDescription: string
  linkData?: YLinkData
  card_sets: YCardSet[] // X
  card_images: YCardImage[] // X
  card_prices: YCardPrice[] // X
}
