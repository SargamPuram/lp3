from collections import Counter, namedtuple
import heapq

class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = Counter(text)
    heap = [Node(char, f, None, None) for char, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    return heap[0] if heap else None

def build_codes(node, prefix='', codebook=None):
    if codebook is None:
        codebook = {}
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + '0', codebook)
        build_codes(node.right, prefix + '1', codebook)
    return codebook

def huffman_encoding(text):
    root = build_huffman_tree(text)
    codes = build_codes(root)
    freq = Counter(text)

    print(f"{'Char':<6} | {'Freq':<5} | Huffman Code")
    print('-' * 30)
    for char, f in freq.items():
        print(f"{repr(char):<6} | {f:<5} | {codes[char]}")

    # Calculate size before compression (assuming 8 bits = 1 char)
    size_before = len(text) * 8  # bits

    # Calculate size after compression
    size_after = 0
    for char, f in freq.items():
        size_after += len(codes[char]) * f

    print('\nSpace Used Before Compression:', size_before, 'bits')
    print('Space Used After Compression:', size_after, 'bits')
    print(f'Compression Ratio: {size_after/size_before:.2f}')

    return codes

if __name__ == "__main__":
    text = input("Enter text to encode: ")
    huffman_encoding(text)

    # abacabad
    # --- ADD THESE LINES ---
    print("\n--- 📊 Complexity Analysis (Detailed) ---")
    print("Full (un-simplified) Time: O(n + k + k*log(k) + k^2)")
    print("Full (un-simplified) Space: O(k + k^2)")
    print("\nFinal (dominant) Time: O(n + k^2)")
    print("Final (dominant) Space: O(k^2)")
    print("(where n = text length, k = unique characters)")
    # -----------------------
