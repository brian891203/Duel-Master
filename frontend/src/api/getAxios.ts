import axios from 'axios'
import { API } from '../config'

export const yugiohBackendAPI = axios.create({
  baseURL: API.YUGIOH_BACKEND,
})
