
import dns.resolver

class SlackIpResolver:
    
    def __init__(self):
        self.resolver = dns.resolver.Resolver()
        # 8.8.8.8 is Google's public DNS server
        self.resolver.nameservers = ['8.8.8.8']

    def resolveIp(self):
        answer = self.resolver.resolve('google.com')

        for data in answer:
            return data
