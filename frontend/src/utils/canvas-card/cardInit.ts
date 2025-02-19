import type { BackCardData, FrontCardData } from 'yugioh-card'
import type { Dimension } from '../../types'
import { setCardImg, setCardScale } from './cardSetting'

export function initFrontCardData(partialFrontCard: Partial<FrontCardData>, size: Dimension) {
  setCardImg(partialFrontCard)
  setCardScale(partialFrontCard, size)
}

export function initBackCardData(partialBackCard: Partial<BackCardData>, size: Dimension) {
  setCardScale(partialBackCard, size)
}
