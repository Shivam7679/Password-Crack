# Password Cracking:

Python code for password cracking: [passcracker.py](https://github.com/Shivam7679/Projects/blob/926ce2a6464718e56bc8a24ea48b915e140b504f/passcracker.py)

To understand this well we can refer to the description below:

In Linux to find hash salt and hash you can refer to the commands below:

```
$sudo cat /etc/shadow
```

*Note: hash salt is referred to the random data generated to add to combine with the original password in order to make the hash more strong

Let us understand with the help of an example:  
Full hash: ````$y$j9T$OAP.Q614fjSxrVbi7hFTX1$XFfcJdQX6/MYYJzx5fiZ4JgSJ519aXkjeiI5hC93SAC````

The hash salt in this case will be : ````$y$j9T$OAP.Q614fjSxrVbi7hFTX1````  
*till the second $ symbol is referred to as hash salt which includes the hashing technique/algorithm

The hash salt is then compared to the full hash and when the decrypted hash matches the word in the password list provided in this case [password.txt](https://github.com/Shivam7679/Projects/blob/6fbc093903bd792636c5a00803e7e6ca71897c27/password.txt) the password is finally cracked.

