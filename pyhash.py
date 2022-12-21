import hashlib
class Blockchain_hashkey:
    def __init__(self,previous_block_hash,transaction_list):
         self.previous_block_hash = previous_block_hash
         self.transaction_list = transaction_list
         self.block_data = "-".join(transaction_list)+"-"+ previous_block_hash
         self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
t1="Vishal sends 2 BTC to vishva"
t2="vishva sends 1.2 BTC to darsan"
t3="darsan sends 1 BTC to ramji"
t4="ramji sends 2.1 BTC to Noble Richard"
initial_block = Blockchain_hashkey("Initial string", [t1, t2])

print("\n",initial_block.block_data)
print("\n",initial_block.block_hash)

second_block =Blockchain_hashkey(initial_block.block_hash,[t3,t4])

print("\n",second_block.block_data)
print("\n",second_block.block_hash)

# finding the length of the hexadecimal addresss for the SHA256 

a=len("431d9ae6e31409bf23ea40cb3447ac3f0e66fe4f16cc3bcaecac27f29f42f3e8")
b=len("e5f4d85aa15e630dbbca6ea007ff1bc5a6259e7742c98817a4d1a4725b7f87d3")
print("\n",a,b)



