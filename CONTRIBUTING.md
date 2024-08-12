# Contribution guide

Thank you for wanting to contribute to this project !

## How to contribute ? 
If you think you have a good idea for a fonctionnaity :

1. Fork the repository
2. Create a branch for your feature (`git checkout -b feature`)
3. Commit your changes (`git commit -m 'Adding a feature'`)
4. Push to the branch (`git push origin feature`)
5. Open a pull request

## How to add irrational numbers ? 

1. For that you need 2 things :
  - A `.txt` file with the decimals in it.
  - A photo of the symbol of the irrational number.
  
  > [!WARNING]
  > The photo can have a maximum dimension of 50x50.

2. Put the `.txt` file in the directory `sources/ressources/decimals`
   
3. Put the photo in the directory `sources/ressources/images`

4. Add the information of the irrational number in the `Irrationals_numbers.json` file.
   Like this :
   ```json
   {
     "name": "name of the irrational number here",
     "image_path": "sources/ressources/images/name_of_your_file.png",
     "decimals_path": "sources/ressources/decimals/name_of_your_file.txt"
   }
   ```

   Example :
   ```json
   {
     "name": "Pi",
     "image_path": "sources/ressources/images/Pi.png",
     "decimals_path": "sources/ressources/decimals/pi.txt"
   }
   ```
