import qrcode

import qrcode
from datetime import datetime
"""
# Function to get the updated link
def get_daily_link():
    # Current date in the desired format (e.g., "2025-01-13")
    today = datetime.now().strftime('%Y-%m-%d')
    # Construct the link with the current date
    base_link = 'https://www.vg.no/'
    daily_link = f"{base_link}{today}"
    return daily_link

# Generate the QR code
def generate_qr_code(link, filename):
    qr = qrcode.QRCode(version=1, box_size=5, border=5)
    qr.add_data(link)
    qr.make()
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(filename)

# Main execution
if __name__ == "__main__":
    daily_link = get_daily_link()
    print(f"Today's link: {daily_link}")
    generate_qr_code(daily_link, 'uib.png')

"""
#whithout updating, little easier 
website_link = 'https://www4.uib.no/program/data-science-integrert-masterprogram-sivilingenior/plan'

qr = qrcode.QRCode(version=1, box_size=5, border=5)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color='black', back_color='white')
img.save('uib.png')
