import type { FrontCardData } from 'yugioh-card'
import type { YCard } from './ygoprodeck'

// * API Response * //
export type TranslateAPIResponse =
  | { success: true, frontCardData: Partial<FrontCardData> }
  | { success: false, errMessage: string }

export type QuestionAPIResponse =
  | { success: true, answer: string }
  | { success: false, errMessage: string }

export type DataAPIResponse =
  | { data: YCard[] }
  | { error: string }
