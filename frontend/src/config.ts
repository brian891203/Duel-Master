type ApiKey = 'AVATAR' | 'YUGIOH_DATA' | 'YUGIOH_BACKEND' | 'YUGIOH_IMAGE' | 'YUGIOH_MATERIAL'
type PathKey = 'YUGIOH_RESOURCES_DIR'

export const API: Record<ApiKey, string> = {
  AVATAR: "https://api.dicebear.com/7.x",
  YUGIOH_DATA: "https://db.ygoprodeck.com/api/v7/cardinfo.php", // ! Not used yet
  YUGIOH_BACKEND: import.meta.env.VITE_YUGIOH_BACKEND_API,
  YUGIOH_IMAGE: `${import.meta.env.VITE_YUGIOH_BACKEND_API}/api/assets/card-image`,
  YUGIOH_MATERIAL: `${import.meta.env.VITE_YUGIOH_BACKEND_API}/api/assets/yugioh-card`,
} as const

export const PATH: Record<PathKey, string> = {
  YUGIOH_RESOURCES_DIR: import.meta.env.VITE_YUGIOH_RESOURCES_DIR,
} as const

export const AVATAR_URLS = {
  System: `${API.AVATAR}/bottts/svg?seed=system`,
  You: `${API.AVATAR}/avataaars/svg?seed=chickenattack`,
} as const

export const CARD_LEAVING_MS = 2500
export const FLIP_DURATION_MS = 1000
export const LARGE_CARD_BP = {
  breakpointMap: {
    320: 260,
    375: 300,
    425: 330,
    768: 350,
    850: 370,
    1024: 400,
  },
  maxSize: { width: 400 },
}
export const SMALL_CARD_BP = {
  breakpointMap: {
    320: 140,
    375: 150,
    425: 165,
    850: 200,
  },
  maxSize: { width: 250 },
}
