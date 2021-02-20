from hashlib import sha256
MAX_NONCE = 1000000000
def SHA256(text):
 return(sha256(text.encode("ascii")).hexdigest())

def mine(block_number,transactions,previous_hash,prefix_zeros):
 prefix_str = '0' * prefix_zeros
 for nonce in range(MAX_NONCE):
   text = str(block_number) + transactions + previous_hash + str(nonce)
   new_hash = SHA256(text)
   if new_hash.startswith(prefix_str):
    print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
    return new_hash 


 raise BaseException(f"couldn't find after {MAX_NONCE} times")

 
if __name__=='__main__':
 transactions='''
 Kaja -> Trojan -> 50
 Emma -> Legend -> 45
    '''

 difficulty = 6
 new_hash = mine(5,transactions,'000000xa036944e29568d0cff17edbe038fecf9a66be992b8321c6ec7',difficulty)
 print(SHA256(new_hash))  