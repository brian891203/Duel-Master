import axios from 'axios'
import { API } from '../config'

export const yugiohImageAPI = axios.create({
  baseURL: API.YUGIOH_IMAGE,
})

export const yugiohBackendAPI = axios.create({
  baseURL: API.YUGIOH_BACKEND,
})
