import cv2
import numpy as np
from heapq import heappush, heappop
from collections import defaultdict
import struct

class HuffmanNode:
    def __init__(self, freq, pixel=None):
        self.freq = freq
        self.pixel = pixel
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequencies(image):
    frequencies = defaultdict(int)
    height, width = image.shape
    for i in range(height):
        for j in range(width):
            frequencies[image[i, j]] += 1
    return frequencies

def build_huffman_tree(frequencies):
    heap = []
    for pixel, freq in frequencies.items():
        node = HuffmanNode(freq, pixel)
        heappush(heap, node)

    while len(heap) > 1:
        left_node = heappop(heap)
        right_node = heappop(heap)
        combined_freq = left_node.freq + right_node.freq
        parent_node = HuffmanNode(combined_freq)
        parent_node.left = left_node
        parent_node.right = right_node
        heappush(heap, parent_node)

    return heap[0]

def build_huffman_codes(node, current_code, huffman_codes):
    if node.pixel is not None:
        huffman_codes[node.pixel] = current_code
        return

    build_huffman_codes(node.left, current_code + '0', huffman_codes)
    build_huffman_codes(node.right, current_code + '1', huffman_codes)

def compress_image(image, huffman_codes):
    compressed_data = ''
    height, width = image.shape
    for i in range(height):
        for j in range(width):
            pixel = image[i, j]
            compressed_data += huffman_codes[pixel]

    padding_size = 8 - len(compressed_data) % 8
    compressed_data += '0' * padding_size
    padding_info = format(padding_size, '08b')
    compressed_data = padding_info + compressed_data

    num_bytes = len(compressed_data) // 8
    byte_data = bytearray()
    for i in range(num_bytes):
        start = i * 8
        end = start + 8
        byte = compressed_data[start:end]
        byte_value = int(byte, 2)
        byte_data.append(byte_value)

    return byte_data

def decompress_image(compressed_data, huffman_tree, original_shape):
    decompressed_data = ''
    for byte in compressed_data:
        byte_binary = format(byte, '08b')
        decompressed_data += byte_binary

    padding_size = int(decompressed_data[:8], 2)
    decompressed_data = decompressed_data[8:-padding_size]

    height, width = original_shape
    decompressed_image = np.empty((height, width), dtype=np.uint8)
    current_node = huffman_tree
    index = 0
    for i in range(height):
        for j in range(width):
            while current_node.left is not None and current_node.right is not None:
                bit = decompressed_data[index]
                if bit == '0':
                    current_node = current_node.left
                else:
                    current_node = current_node.right
                index += 1
            decompressed_image[i, j] = current_node.pixel
            current_node = huffman_tree

    return decompressed_image

# Load gambar menggunakan OpenCV
image_path = "colorful.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
orimage = cv2.imread(image_path)

# Tentukan tingkat kuantisasi
quantization_levels = 10

# Kuantisasi gambar
quantized_image = cv2.convertScaleAbs(image, alpha=(quantization_levels / 255))

# Menghitung frekuensi kemunculan setiap nilai piksel dalam gambar kuantisasi
if quantized_image is not None:
    frequencies = calculate_frequencies(quantized_image)
else:
    print("Error: Failed to quantize the image.")

# Membangun pohon Huffman
huffman_tree = build_huffman_tree(frequencies)

# Membangun tabel kode Huffman
huffman_codes = {}
build_huffman_codes(huffman_tree, '', huffman_codes)

# Kompresi gambar menggunakan kode Huffman
compressed_data = compress_image(quantized_image, huffman_codes)

# Simpan tabel kode Huffman dan data terkompresi ke file
with open("compressed_data.bin", "wb") as file:
    file.write(struct.pack('B' * len(compressed_data), *compressed_data))

# Baca data terkompresi dari file
with open("compressed_data.bin", "rb") as file:
    compressed_data = file.read()

# Dekompresi gambar menggunakan kode Huffman
decompressed_image = decompress_image(compressed_data, huffman_tree, quantized_image.shape)

# Tampilkan gambar asli dan gambar yang telah dikuantisasi dan didekompresi
cv2.imshow("Original " , orimage)
cv2.imshow("Monokrom Image", image)
cv2.imshow("Quantized and Decompressed Image", decompressed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
