class Solution(object):
    def numUniqueEmails(self, emails):
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]  # Ignore everything after '+'
            local = local.replace('.', '')  # Remove all '.'
            unique_emails.add(local + '@' + domain)  # Recombine local and domain
        
        return len(unique_emails)
emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
sol = Solution()
print(sol.numUniqueEmails(emails)) 
