import type { AxiosResponse } from 'axios'
import type { QuestionAPIResponse } from '../types'
import { yugiohBackendAPI } from './getAxios'

export function questionAPI(text: string): Promise<AxiosResponse<QuestionAPIResponse>> {
  return yugiohBackendAPI.post('/api/question', text, {
    headers: {
      'Content-Type': 'text/plain',
    },
  })
}
