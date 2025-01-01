import type { AxiosResponse } from 'axios'
import axios from 'axios'
import { API } from '../config'
import type { DataAPIResponse } from '../types/response'

// YGOProDeck API
export function dataAPI(password: string): Promise<AxiosResponse<DataAPIResponse>> {
  return axios.get(API.YUGIOH_DATA, { params: { id: password } })
}
