![Screenshot 2025-01-03 155345](https://github.com/user-attachments/assets/007c3ada-afa8-40cd-975d-5bc5d9542090)

---

### Steps to Run the Script on Ubuntu

1. **Update System Packages**  
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Python**  
   ```bash
   sudo apt install python3 python3-pip -y
   ```

3. **Install Required Python Libraries**  
   ```bash
   pip3 install requests rich
   ```

4. **Create and Edit the `wallets.txt` File**  
   Use `nano` to create the file and add wallet addresses:
   ```bash
   nano wallets.txt
   ```
   
   **Each line should contain **only the wallet address**, without any additional characters, commas, or spaces. as follows:

   ```plaintext
   eg_wallet_address_1
   eg_wallet_address_2
   ```
   Save and exit:
   - Press `CTRL + O` to save.
   - Press `Enter` to confirm.
   - Press `CTRL + X` to exit.

5. **Run the Script**  
   Execute the script using Python:
   ```bash
   python3 checker.py
   ```

6. **Check the Results**  
   After running, view the output in the `results.txt` file:
   ```bash
   cat results.txt
   ```
   
