# key-split

Two tiny Python scripts to split a string into two hex-encoded shares using XOR, and to recombine those shares back into the original string.

Useful for sharing a secret across two people (both shares required) or sending it over two separate channels so compromising one channel alone doesn’t reveal the secret.

## Requirements

- Python 3

## Usage

### Split

`split.py` takes a plaintext string and prints two lines:

1) a random pad (hex)
2) the XOR of the plaintext bytes with that pad (hex)

```bash
$ ./split.py "hello world"
c930646d6c7039391a3ea2
a155080103504e566852c6
```

### Combine

`combine.py` takes the two hex strings (pad and xor output) and prints the recovered plaintext.

```bash
$ ./combine.py c930646d6c7039391a3ea2 a155080103504e566852c6
hello world
```
