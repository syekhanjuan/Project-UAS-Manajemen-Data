#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo "Tolong jalankan script ini menggunakan sudo."
  exit
fi

FILE="daftar_user.txt"

if [ ! -f "$FILE" ]; then
    echo "File $FILE tidak ditemukan!"
    exit 1
fi

while IFS= read -r username; do
    if id "$username" &>/dev/null; then
        echo "User $username sudah terdaftar."
    else
        useradd -m -s /bin/bash "$username"
        echo "$username:$username@123" | chpasswd
        echo "Berhasil: User '$username' dibuat dengan password '$username@123'"
    fi
done < "$FILE"
