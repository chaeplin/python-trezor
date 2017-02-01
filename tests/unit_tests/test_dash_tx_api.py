# This file is part of the TREZOR project.
#
# Copyright (C) 2012-2016 Marek Palatinus <slush@satoshilabs.com>
# Copyright (C) 2012-2016 Pavol Rusnak <stick@satoshilabs.com>
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.

import unittest
import random

from trezorlib import tx_api
from trezorlib.tx_api import TxApiDash, TxApiDashTestnet


class TestTxApi(unittest.TestCase):

    def testmainnet_get(self):
        exp = [
            'http://insight.dev.dash.org/api',
            'https://blockchain.masternode.io/api',
            'http://insight.dash.org/insight-api-dash',
            'https://insight.dash.siampm.com/api',
            'http://insight.masternode.io:3000/api'
        ]

        tx_api.urldash = exp[random.randrange(0,len(exp))]
        print(tx_api.urldash)
        tx = TxApiDash.get_tx('a21f516c2789906e5826e976b4b178fcb864feb8e36d2728cf52cfe0c4895f8d')

        tx_api.urldash = exp[random.randrange(0,len(exp))]
        print(tx_api.urldash)
        tx = TxApiDash.get_tx('9e220531379e5ae1a433be57f7f750bf073985120589019d8dc2c90b748d08c0')
        
        tx_api.urldash = exp[random.randrange(0,len(exp))]
        print(tx_api.urldash)
        tx = TxApiDash.get_tx('32b1069882114a895bf75020ad340ffa9b498b0062359e6ebd66c1df0181e803')
        
        tx_api.urldash = exp[random.randrange(0,len(exp))]
        print(tx_api.urldash)
        tx = TxApiDash.get_tx('d174363ec078ceeeeed4b39a8fb5fe0096195f0552ab1f89a25120aa7768ed29')
        
        tx_api.urldash = exp[random.randrange(0,len(exp))]
        print(tx_api.urldash)
        tx = TxApiDash.get_tx('bbb73334a71101d5741cd4482bdfb36e7ac2ef8941e0900d11d108d58ca37828')

    def testnetnet_get(self):
        tx_api.urldash = 'https://test.insight.dash.siampm.com/api'
        print(tx_api.urldash)
        tx = TxApiDashTestnet.get_tx('65e796b037bbb9b30ef43a21c73505cc3a059706f57a0cd9090e9bc19fe1fe15')
        tx = TxApiDashTestnet.get_tx('e4c305bdfd4fda7b992fc053fe091c9f5da7ec185519573601fea4a7f9dae700')

if __name__ == '__main__':
    unittest.main()
