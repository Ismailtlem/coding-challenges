# Challenge 1 - Write your own wc tool

This challenge corresponds to the first part of the Coding Challenges series by John Crickett https://codingchallenges.fyi/challenges/challenge-wc.

## Description

The WC tool is written in `wc.py` file. The tool is used to count the number of words, lines, bytes and characters in a file/stdin.

## Usage

If you have a virtualenv set up, you can just run the cli like the following

```bash
python wc.py -p filename [option]
```

The following options are supported:

- `-w`: prints the number of words in the file
- `-l`: prints the number of lines in the file
- `-c`: prints the number of bytes in the file
- `-m`: prints the number of characters in the file

The tool can also be used in stdin mode as follows:

```bash
cat filename | python wc.py -p filename [option]
```
