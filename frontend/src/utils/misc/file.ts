import type { DataTypesChecker } from '../../types'

export function fileToBase64(file: File): Promise<string> {
  return new Promise((resolve) => {
    const reader = new FileReader()
    reader.onload = () => resolve(reader.result as string)
    reader.readAsDataURL(file)
  })
}

export function isImage(types: readonly string[]): boolean {
  // * 因為 Imgur 不支援 upload webp 格式，所以這裡要排除 webp
  return types.every(type => type.startsWith('image') && type !== 'image/webp')
}

export function checkDataTypes(types: string | string[], dataTypes: DataTypesChecker): boolean {
  const typeArray = Array.isArray(types) ? types : [types]
  return typeof dataTypes === 'function'
    ? dataTypes(typeArray)
    : dataTypes.some(item => typeArray.includes(item))
}

export function extractFile(event: Event, dataTypes: DataTypesChecker): File | undefined {
  const fileInput = event.target as HTMLInputElement
  if (fileInput.files?.length) {
    const file = fileInput.files[0]
    fileInput.value = '' // Reset input field
    if (checkDataTypes(file.type, dataTypes)) {
      return file
    }
    else {
      alert('Please upload a valid file!')
    }
  }
}
