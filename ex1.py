import re

text="To take things up a notch, #leo I’ve integrated digital-specific syntax like social media handles, active web links, https?:leo_das_ and blockchain-style tokens into the mix.The Ultimate Character & Syntax Stress TestHey @Digital_Nomad! 🌐 Check out the latest update at https://example.com/system-test?id=404. I just sent the report to support.center_2026@domain.io. We’re seeing a massive surge in the #TechRevolution tag! 🚀 The smart contract executed for 0.0052 ETH (Token: 0x71C91B151535394a3A2711EE01) at exactly 15:30:45.If we calculate the variance where $\sigma^{2} = \frac{\sum (x - \mu)^{2}}{N}$, the results are [100%] accurate. 📊 However, the server logs showed: GET /api/v1/users/admin_root_#99. Is this a ⚠️ glitch or a feature? {Response: Unknown}. ¡Hola! ¿Cómo estás? (Hi! How are you?)."

hashtaags=re.findall(r"#\+",text)
mentions=re.findall(r"@\w+",text)
emails=re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b",text)
urls=re.findall(r"https?:/^S+",text)
dates=re.findall(r"\b\d{1,2}^d{1,2,}^d{4}\b",text)
tokens=re.findall(r"\b\w+\b",text)


print("Hashtags:",hashtaags)
print("Mentions:",mentions)
print("Emails:",emails)
print("URLs:",urls)
print("Dates:",dates)
print("Tokens:",tokens)
