from scapy.all import sniff

def process_packet(packet):
    print(f"📦 Packet: {packet.summary()}")

def main():
    print("🔍 Starting packet capture (Press Ctrl+C to stop)...")
    
    # Capture 0 = unlimited, prn = callback to process each packet
    sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    main()
