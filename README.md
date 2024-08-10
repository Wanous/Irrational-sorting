# Irrational-sorting [π]
<div align="center"><img alt="banniere" align="center"  height="50%" width="100%" src="photos/TPI_banner.png"></div>

<div align=center>
  <img alt="Taille du code GitHub" src="https://img.shields.io/github/languages/code-size/Wanous/Irrational-sorting?label=taille%20du%20code">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Wanous/Irrational-sorting?logo=github&style=plastic">
  <img alt="License" src="https://img.shields.io/github/license/Wanous/Irrational-sorting?style=plastic">
</div>
<br>

The Irrational sorting algorithm is an innovative method that uses irrational numbers to organize data. Specifically, it leverages the unique properties of these numbers to create a sequence that can sort a list of items in an unconventional way. 

## How it works ?
I sort the items by repeatedly swapping their positions based on the digits of the Irrational number used. For example, if the first two digits of the irrational number are 1 and 2, you would swap the first and second items in your list. You continue this process, using more digits as needed, depending on the size of the list.

## Handling Larger Lists
The algorithm adapts to different list sizes by using more digits from the irrational number as the list grows. For a list of 10 items, you use one digit at a time; for a list of 100 items, you use two digits at a time, and so on. This ensures that every item in the list can be properly sorted, even as the list size increases.

I calculate that with this equation : p = ⌈log10(n)⌉
- p non-zero natural integer
- n non-zero natural integer (a list can't be empty)
