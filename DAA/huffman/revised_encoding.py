import heapq

# Define Node class manually
class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char      # Character or None if internal node
        self.freq = freq      # Frequency of character(s)
        self.left = left      # Left child node
        self.right = right    # Right child node

    # Define less than for priority queue ordering by frequency
    def __lt__(self, other):
        return self.freq < other.freq


def count_frequency(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq


def build_huffman_tree(text):
    freq = count_frequency(text)
    heap = []

    # Create leaf nodes for each character and push to heap
    for ch, f in freq.items():
        heapq.heappush(heap, Node(ch, f))

    # Merge nodes until one tree remains
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
        # Leaf node
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + '0', codebook)
        build_codes(node.right, prefix + '1', codebook)
    return codebook


def huffman_encoding(text):
    root = build_huffman_tree(text)
    codes = build_codes(root)
    freq = count_frequency(text)

    print(f"{'Char':<6} | {'Freq':<5} | Huffman Code")
    print('-' * 30)
    for ch, f in freq.items():
        print(f"{repr(ch):<6} | {f:<5} | {codes[ch]}")

    # Calculate and display space used before and after compression
    size_before = len(text) * 8
    size_after = sum(len(codes[ch]) * f for ch, f in freq.items())
    print('\nSpace Used Before Compression:', size_before, 'bits')
    print('Space Used After Compression:', size_after, 'bits')
    print(f'Compression Ratio: {size_after/size_before:.2f}')

    return codes


if __name__ == "__main__":
    text = input("Enter text to encode: ")
    huffman_encoding(text)
