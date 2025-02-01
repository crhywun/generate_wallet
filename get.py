from web3 import Web3
import time

# 配置你的节点或服务端点
base_sep = "https://base_sepolia.g.alchemy.com/v2/M6nt5EmGRZYKykiYAGzf1Ad2AUgOt8XT"  # 替换成你的以太坊节点或服务端点
op_sep = "https://opt_sepolia.g.alchemy.com/v2/M6nt5EmGRZYKykiYAGzf1Ad2AUgOt8XT"  # Binance智能链的公共节点

# 创建Web3实例
web3_eth = Web3(Web3.HTTPProvider(base_sep))
web3_bsc = Web3(Web3.HTTPProvider(op_sep))

# 检查是否成功连接
if not web3_eth.is_connected():
    print("Failed to connect to base_sep node.")
else:
    print("Connected to base_sep node.")

if not web3_bsc.is_connected():
    print("Failed to connect to op_sep node.")
else:
    print("Connected to op_sep node.")

# 设置要检查的地址
address1 = '0x10A3b056Ae67D27dC15d45C8CFD0cC275C456ac4'  # 在以太坊上的地址
address2 = '0xb02d04799604daefd22f9311d8d9a78758295a95'  # 在Binance智能链上的地址

def check_balances():
    # 查询并打印以太坊上的余额
    base_eth = web3_eth.eth.get_balance(address1)
    print(f"Address {address1} on base_sep has balance: {web3_eth.fromWei(base_eth, 'ether')} ETH")

    base_eth1 = web3_eth.eth.get_balance(address2)
    print(f"Address {address1} on base_sep has balance: {web3_eth.fromWei(base_eth1, 'ether')} ETH")
    
    # 查询并打印Binance智能链上的余额
    op_eth = web3_bsc.eth.get_balance(address2)
    print(f"Address {address2} on op_sep has balance: {web3_bsc.fromWei(op_eth, 'ether')} BNB")
    op_eth1 = web3_bsc.eth.get_balance(address2)
    print(f"Address {address2} on op_sep has balance: {web3_bsc.fromWei(op_eth1, 'ether')} BNB")

while True:
    check_balances()
    time.sleep(1)  # 每隔一秒执行一次