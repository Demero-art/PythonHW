from address import Address
from mailing import Mailing

to_address = Address("706801", "Zarafshan", "12mikroraion", "20", "9")
from_address = Address("650000", "Kemerovo", "Stroiteley", "19", "113")

mailing = Mailing(to_address, from_address, 2500, 854752211)
print(mailing)