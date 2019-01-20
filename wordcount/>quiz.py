from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcNgjBIMM4kniBxy6NP9H78Q7Pmb4pYV1zocfVuvDM44sFHEW0mSi4IGPCD5Jq22xRjJPtEVazmXe-UshwyLDoguTyjvfZkIHjik-fcv7C3ogUoM3zyeNV8wmcgTfPIDAfL61yTBRLvkqCb6ZGuMtdYRXjCUfhWAce7SkhtE5O-w6Uf2xmgaqqUb-Jx16ITZ7rZvmN'

#def main():
f = Fernet(key)
print(f.decrypt(message))


#if __name__ != "__main__":
#    main()