import { type DataTypesChecker } from '../../types'

export const fileToBase64 = (file: File): Promise<string> => {
  return new Promise((resolve) => {
    const reader = new FileReader()
    reader.onload = () => resolve(reader.result as string)
    reader.readAsDataURL(file)
  })
}

export const isImage = (types: readonly string[]): boolean => {
  return types.every((type) => type.startsWith('image'))
}

export const checkDataTypes = (types: string | string[], dataTypes: DataTypesChecker): boolean => {
  const typeArray = Array.isArray(types) ? types : [types]
  return typeof dataTypes === 'function'
    ? dataTypes(typeArray)
    : dataTypes.some((item) => typeArray.includes(item))
}

export const extractFile = (event: Event, dataTypes: DataTypesChecker): File | undefined => {
  const fileInput = event.target as HTMLInputElement
  if (fileInput.files?.length) {
    const file = fileInput.files[0]
    fileInput.value = '' // Reset input field
    if (checkDataTypes(file.type, dataTypes)) {
      return file
    } else {
      alert('Please upload a valid file!')
    }
  }
}
