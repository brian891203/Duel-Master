import type { AxiosResponse } from 'axios'
import type { DataAPIResponse } from '../types/response'
import axios from 'axios'
import { API } from '../config'

// YGOProDeck API
export function dataAPI(password: string): Promise<AxiosResponse<DataAPIResponse>> {
  return axios.get(API.YUGIOH_DATA, { params: { id: password } })
}
