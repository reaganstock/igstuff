
-   Overview
-   ACTIVATION API. V2 [ACTUAL]
    -   Quick start
    -   Data list
    -   All requests
-   Rental service API. v1 [ACTUAL]
    -   Quick start
    -   Data list
    -   All requests
-   ACTIVATION API. ALTERNATIVE
    -   Quick start
    -   Data list
    -   All requests
    -   Errors
-   ACTIVATION API. V1 [DEPRECATED]
    -   Quick start
    -   Data list
    -   All requests
    -   General provisions and list of errors

[![redocly logo](https://cdn.redoc.ly/redoc/logo-mini.svg)API docs by Redocly](https://redocly.com/redoc/)

SMSPVA API Documentaion (1.0.0)
===============================

[](https://docs.smspva.com/#section/Overview)Overview
=====================================================

### The documentation for the SMSPVA.com website is organized into four key sections:

1.  [Main API Documentation for the Activation Section (Version 2)](https://docs.smspva.com/#tag/activation_v2_fast_start)
2.  [Main API Documentation for the Rental Section (Version 1)](https://docs.smspva.com/#tag/rent_fast_start)
3.  [Alternative API Documentation for the Activation Section](https://docs.smspva.com/#tag/activation_alternative_fast_start)
4.  [Deprecated API Documentation for the Activation Section (Version 1)](https://docs.smspva.com/#tag/activation_fast_start)

### Each API Section Includes:

-   **Quick Start:** Basic methods for getting started.
-   **Data List:** A list of services, countries, etc.
-   **All Requests:** A comprehensive list of requests with detailed explanations and examples.

### ApiKey:

Your ApiKey is located in **[the Profile and ApiKey section](https://smspva.com/api/redoc/profile-pass.php)**, accessible via the top right drop-down menu.

### Support:

For any issues, inquiries, or feedback, please contact technical support via [the Help page](https://smspva.com/help.html) or online support chat.

### Specific Instructions for the Activation API:

-   **SMS Reception Timing:** If you haven't received an SMS within 580 seconds (9 minutes and 40 seconds), make sure to ban the number you received. Attempting to ban the number after 10 minutes will result in the number not being banned and potentially being allocated again due to the system retaining the request ID for 10 minutes before its deletion.
-   **Connection rate limit:** Up to 50 connections per seconds are allowed.
-   **Query Interval:** Maintain an interval of 4 to 5 seconds between any queries to ensure full API utilization. Failure to adhere to this may lead to server rejection of your requests.

[](https://docs.smspva.com/#tag/activation_v2_fast_start)Quick start
====================================================================

[](https://docs.smspva.com/#tag/activation_v2_fast_start/paths/~1activation~1number~1{country}~1{service}/get)Get Number
------------------------------------------------------------------------------------------------------------------------

Get a number for country and service

##### Authorizations:

*apikey*

##### path Parameters

| country

required

 |

string

Example: RU

Country 2 symbols name in ISO 3166-2 format, uppercase.\
[Countries list](https://docs.smspva.com/#tag/activation_v2_lists/Countries-list)

 |
| service

required

 |

string

Example: opt20

Service code.\
[Services list](https://docs.smspva.com/#tag/activation_v2_lists/Services-list)

 |

### Responses

**200**

Successful operation

##### Response Schema: application/json

| statusCode |

integer

Example: "200"

Result status code

 |
| data |

object

Response data

 |

**405**

Invalid parameters

**407**

Your balance is too low to receive sms for selected country and service.

**411**

API access limited by low karma or ratelimits

**500**

Failed to fetch number

**501**

Number not found

**502**

Number not found.

**503**

Server overload, try later.

get/activation/number/{country}/{service}

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url https://api.smspva.com/activation/number/RU/opt20\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200
-   405
-   407
-   411
-   500
-   501
-   502
-   503

Content type

application/json

Copy

Expand allCollapse all

`{

-   "statusCode": 200,

-   "data": {

    -   "orderId": 123456,

    -   "phoneNumber": 9876544321,

    -   "countryCode": "RU",

    -   "orderExpireIn": 600

    }

}`

[](https://docs.smspva.com/#tag/activation_v2_fast_start/paths/~1activation~1sms~1{orderid}/get)Receive SMS
-----------------------------------------------------------------------------------------------------------

Receive SMS with service activation code

##### path Parameters

| orderid

required

 |

integer

Example: 123456

ID of order received in number response

 |

##### header Parameters

| partnerkey |

string

Example: 3eaa1c1f977d5a8152380f13cdfd03d0

Optional **partnerkey** parameter for referral system.

 |

### Responses

**200**

Successful operation

##### Response Schema: application/json

| statusCode |

integer

Example: "200"

Result status code

 |
| data |

object

Response data

 |

**202**

SMS not yet received

##### Response Schema: application/json

| statusCode |

integer

Example: "202"

Result status code

 |
| error |

object

Error data

 |

**405**

Invalid parameters

**406**

Order ID format is invalid or not found

**407**

We received SMS but your balance is not enough to pay it.

**410**

This order is closed and unavailable

##### Response Schema: application/json

| statusCode |

integer

Example: "410"

Result status code

 |
| error |

object

Error data

 |

**411**

API access limited by low karma or ratelimits

**500**

Failed to fetch SMS.

**501**

Server failed to process request.

**503**

The server is overloaded and experiencing performance issues. Please try later.

get/activation/sms/{orderid}

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url https://api.smspva.com/activation/sms/123456\
  --header 'partnerkey: SOME_STRING_VALUE'

### Response samples

-   200
-   202
-   405
-   406
-   407
-   410
-   411
-   500
-   501
-   503

Content type

application/json

Copy

Expand allCollapse all

`{

-   "statusCode": 200,

-   "data": {

    -   "sms": {},

    -   "orderId": "123456",

    -   "orderExpireIn": 600

    }

}`

[](https://docs.smspva.com/#tag/activation_v2_lists)Data list
=============================================================

[](https://docs.smspva.com/#tag/activation_v2_lists/Countries-list)Countries list
=================================================================================

For select the country you need - indicate according country code at the "country" parameter.

| № | Flag | Country | Code |
| --- | --- | --- | --- |
| 1 | ![](https://smspva.com/templates/New_theme/images/flags/64/US.png) | United States | US |
| 2 | ![](https://smspva.com/templates/New_theme/images/flags/64/CA.png) | Canada | CA |
| 3 | ![](https://smspva.com/templates/New_theme/images/flags/64/UK.png) | Unt. Kingdom | UK |
| 4 | ![](https://smspva.com/templates/New_theme/images/flags/64/FR.png) | France | FR |
| 5 | ![](https://smspva.com/templates/New_theme/images/flags/64/DE.png) | Germany | DE |
| 6 | ![](https://smspva.com/templates/New_theme/images/flags/64/IT.png) | Italy | IT |
| 7 | ![](https://smspva.com/templates/New_theme/images/flags/64/ES.png) | Spain | ES |
| 8 | ![](https://smspva.com/templates/New_theme/images/flags/64/AL.png) | Albania | AL |
| 9 | ![](https://smspva.com/templates/New_theme/images/flags/64/AR.png) | Argentina | AR |
| 10 | ![](https://smspva.com/templates/New_theme/images/flags/64/AU.png) | Australia | AU |
| 11 | ![](https://smspva.com/templates/New_theme/images/flags/64/AT.png) | Austria | AT |
| 12 | ![](https://smspva.com/templates/New_theme/images/flags/64/BD.png) | Bangladesh | BD |
| 13 | ![](https://smspva.com/templates/New_theme/images/flags/64/BA.png) | Bos. and Herz. | BA |
| 14 | ![](https://smspva.com/templates/New_theme/images/flags/64/BR.png) | Brazil | BR |
| 15 | ![](https://smspva.com/templates/New_theme/images/flags/64/BG.png) | Bulgaria | BG |
| 16 | ![](https://smspva.com/templates/New_theme/images/flags/64/KH.png) | Cambodia | KH |
| 17 | ![](https://smspva.com/templates/New_theme/images/flags/64/CM.png) | Cameroon | CM |
| 18 | ![](https://smspva.com/templates/New_theme/images/flags/64/CL.png) | Chile | CL |
| 19 | ![](https://smspva.com/templates/New_theme/images/flags/64/CO.png) | Colombia | CO |
| 20 | ![](https://smspva.com/templates/New_theme/images/flags/64/HR.png) | Croatia | HR |
| 21 | ![](https://smspva.com/templates/New_theme/images/flags/64/CY.png) | Cyprus | CY |
| 22 | ![](https://smspva.com/templates/New_theme/images/flags/64/CZ.png) | Czech Republic | CZ |
| 23 | ![](https://smspva.com/templates/New_theme/images/flags/64/DK.png) | Denmark | DK |
| 24 | ![](https://smspva.com/templates/New_theme/images/flags/64/DO.png) | Dominicana | DO |
| 25 | ![](https://smspva.com/templates/New_theme/images/flags/64/EG.png) | Egypt | EG |
| 26 | ![](https://smspva.com/templates/New_theme/images/flags/64/EE.png) | Estonia | EE |
| 27 | ![](https://smspva.com/templates/New_theme/images/flags/64/FI.png) | Finland | FI |
| 28 | ![](https://smspva.com/templates/New_theme/images/flags/64/GE.png) | Georgia | GE |
| 29 | ![](https://smspva.com/templates/New_theme/images/flags/64/GH.png) | Ghana (Virtual) | GH |
| 30 | ![](https://smspva.com/templates/New_theme/images/flags/64/GI.png) | Gibraltar | GI |
| 31 | ![](https://smspva.com/templates/New_theme/images/flags/64/GR.png) | Greece | GR |
| 32 | ![](https://smspva.com/templates/New_theme/images/flags/64/HK.png) | Hong Kong | HK |
| 33 | ![](https://smspva.com/templates/New_theme/images/flags/64/HU.png) | Hungary | HU |
| 34 | ![](https://smspva.com/templates/New_theme/images/flags/64/IN.png) | India | IN |
| 35 | ![](https://smspva.com/templates/New_theme/images/flags/64/JP.png) | Japan | JP |
| 36 | ![](https://smspva.com/templates/New_theme/images/flags/64/KG.png) | Kyrgyzstan (Virtual) | KG |
| 37 | ![](https://smspva.com/templates/New_theme/images/flags/64/MT.png) | Malta | MT |
| 38 | ![](https://smspva.com/templates/New_theme/images/flags/64/NO.png) | Norway | NO |
| 39 | ![](https://smspva.com/templates/New_theme/images/flags/64/PK.png) | Pakistan (Virtual) | PK |
| 40 | ![](https://smspva.com/templates/New_theme/images/flags/64/SA.png) | Saudi Arabia | SA |
| 41 | ![](https://smspva.com/templates/New_theme/images/flags/64/SG.png) | Singapore | SG |
| 42 | ![](https://smspva.com/templates/New_theme/images/flags/64/CH.png) | Switzerland | CH |
| 43 | ![](https://smspva.com/templates/New_theme/images/flags/64/TZ.png) | Tanzania | TZ |
| 44 | ![](https://smspva.com/templates/New_theme/images/flags/64/UZ.png) | Uzbekistan (Virtual) | UZ |
| 45 | ![](https://smspva.com/templates/New_theme/images/flags/64/ID.png) | Indonesia | ID |
| 46 | ![](https://smspva.com/templates/New_theme/images/flags/64/IE.png) | Ireland | IE |
| 47 | ![](https://smspva.com/templates/New_theme/images/flags/64/IL.png) | Israel | IL |
| 48 | ![](https://smspva.com/templates/New_theme/images/flags/64/KZ.png) | Kazakhstan | KZ |
| 49 | ![](https://smspva.com/templates/New_theme/images/flags/64/KE.png) | Kenya | KE |
| 50 | ![](https://smspva.com/templates/New_theme/images/flags/64/LA.png) | Laos | LA |
| 51 | ![](https://smspva.com/templates/New_theme/images/flags/64/LV.png) | Latvia | LV |
| 52 | ![](https://smspva.com/templates/New_theme/images/flags/64/LT.png) | Lithuania | LT |
| 53 | ![](https://smspva.com/templates/New_theme/images/flags/64/MK.png) | Macedonia | MK |
| 54 | ![](https://smspva.com/templates/New_theme/images/flags/64/MY.png) | Malaysia | MY |
| 55 | ![](https://smspva.com/templates/New_theme/images/flags/64/MX.png) | Mexico | MX |
| 56 | ![](https://smspva.com/templates/New_theme/images/flags/64/MD.png) | Moldova | MD |
| 57 | ![](https://smspva.com/templates/New_theme/images/flags/64/MA.png) | Morocco | MA |
| 58 | ![](https://smspva.com/templates/New_theme/images/flags/64/NL.png) | Netherlands | NL |
| 59 | ![](https://smspva.com/templates/New_theme/images/flags/64/NZ.png) | New Zealand | NZ |
| 60 | ![](https://smspva.com/templates/New_theme/images/flags/64/NG.png) | Nigeria | NG |
| 61 | ![](https://smspva.com/templates/New_theme/images/flags/64/PY.png) | Paraguay | PY |
| 62 | ![](https://smspva.com/templates/New_theme/images/flags/64/PH.png) | Philippines | PH |
| 63 | ![](https://smspva.com/templates/New_theme/images/flags/64/PL.png) | Poland | PL |
| 64 | ![](https://smspva.com/templates/New_theme/images/flags/64/PT.png) | Portugal | PT |
| 65 | ![](https://smspva.com/templates/New_theme/images/flags/64/RO.png) | Romania | RO |
| 66 | ![](https://smspva.com/templates/New_theme/images/flags/64/RU.png) | Russian Federation | RU |
| 67 | ![](https://smspva.com/templates/New_theme/images/flags/64/RS.png) | Serbia | RS |
| 68 | ![](https://smspva.com/templates/New_theme/images/flags/64/SK.png) | Slovakia | SK |
| 69 | ![](https://smspva.com/templates/New_theme/images/flags/64/SI.png) | Slovenia | SI |
| 70 | ![](https://smspva.com/templates/New_theme/images/flags/64/ZA.png) | South Africa | ZA |
| 71 | ![](https://smspva.com/templates/New_theme/images/flags/64/SE.png) | Sweden | SE |
| 72 | ![](https://smspva.com/templates/New_theme/images/flags/64/TH.png) | Thailand | TH |
| 73 | ![](https://smspva.com/templates/New_theme/images/flags/64/TR.png) | Turkey | TR |
| 74 | ![](https://smspva.com/templates/New_theme/images/flags/64/UA.png) | Ukraine | UA |
| 75 | ![](https://smspva.com/templates/New_theme/images/flags/64/VN.png) | Vietnam | VN |

[](https://docs.smspva.com/#tag/activation_v2_lists/Services-list)Services list
===============================================================================

If you do not find the service you need, then you can use the OTHER (opt19) service or contact support to add the service you need.

| № | Logo | Service | Code |
| --- | --- | --- | --- |
| 1 | ![](https://smspva.com/templates/New_Design/images/ico/open_api.png "service-img") | 1 OpenAI API (chatGPT, DALL-e 2) | opt132 |
| 2 | ![](https://smspva.com/templates/New_Design/images/ico/opt251_66e125780140b.jpg "service-img") | 1cupis.ru | opt251 |
| 3 | ![](https://smspva.com/templates/New_Design/images/ico/opt224_66068262d71e1.png "service-img") | 22bet | opt224 |
| 4 | ![](https://smspva.com/templates/New_Design/images/ico/opt22_655cdab4dbd01.jpg "service-img") | 888casino | opt22 |
| 5 | ![](https://smspva.com/templates/New_Design/images/ico/opt242_668e3f109c6d0.png "service-img") | Abbott | opt242 |
| 6 | ![](https://smspva.com/templates/New_Design/images/ico/nike.png "service-img") | Adidas & Nike | opt86 |
| 7 | ![](https://smspva.com/templates/New_Design/images/ico/airbnb.ico "service-img") | Airbnb | opt46 |
| 8 | ![](https://smspva.com/templates/New_Design/images/ico/taobao.png "service-img") | Alibaba (Taobao, 1688.com) | opt61 |
| 9 | ![](https://smspva.com/templates/New_Design/images/ico/amazon.ico "service-img") | Amazon | opt44 |
| 10 | ![](https://smspva.com/templates/New_Design/images/ico/aol.png "service-img") | AOL | opt10 |
| 11 | ![](https://smspva.com/templates/New_Design/images/ico/apple.ico "service-img") | Apple | opt131 |
| 12 | ![](https://smspva.com/templates/New_Design/images/ico/opt143_655cd99229dba.jpg "service-img") | autocosmos.com | opt143 |
| 13 | ![](https://smspva.com/templates/New_Design/images/ico/avito.png "service-img") | Avito | opt59 |
| 14 | ![](https://smspva.com/templates/New_Design/images/ico/badoo.png "service-img") | Badoo | opt56 |
| 15 | ![](https://smspva.com/templates/New_Design/images/ico/opt209_65801c9cb87c2.png "service-img") | BANDUS | opt209 |
| 16 | ![](https://smspva.com/templates/New_Design/images/ico/opt138_655b124b5ce53.png "service-img") | Bazos.sk | opt138 |
| 17 | ![](https://smspva.com/templates/New_Design/images/ico/opt187_655ca45c48943.png "service-img") | Beget.com | opt187 |
| 18 | ![](https://smspva.com/templates/New_Design/images/ico/opt252_6729d8ff99907.png "service-img") | Best Buy | opt252 |
| 19 | ![](https://smspva.com/templates/New_Design/images/ico/bet365.png "service-img") | bet365 | opt17 |
| 20 | ![](https://smspva.com/templates/New_Design/images/ico/opt192_656ef71f9770d.jpg "service-img") | Betano (+BETANO.ro) | opt192 |
| 21 | ![](https://smspva.com/templates/New_Design/images/ico/betfair.png "service-img") | BetFair | opt25 |
| 22 | ![](https://smspva.com/templates/New_Design/images/ico/opt223_6605370e23fca.jpg "service-img") | Betmgm | opt223 |
| 23 | ![](https://smspva.com/templates/New_Design/images/ico/opt237_66617efa9abc1.png "service-img") | Bitpanda | opt237 |
| 24 | ![](https://smspva.com/templates/New_Design/images/ico/blizzard.ico "service-img") | Blizzard | opt78 |
| 25 | ![](https://smspva.com/templates/New_Design/images/ico/opt135_66630426565d2.png "service-img") | blsspain-russia.com | opt135 |
| 26 | ![](https://smspva.com/templates/New_Design/images/ico/bolt.png "service-img") | Bolt | opt81 |
| 27 | ![](https://smspva.com/templates/New_Design/images/ico/opt217_65c5907f769ab.png "service-img") | Brevo | opt217 |
| 28 | ![](https://smspva.com/templates/New_Design/images/ico/opt145_666304863ecdf.png "service-img") | bumble | opt145 |
| 29 | ![](https://smspva.com/templates/New_Design/images/ico/opt199_6578544374956.png "service-img") | bunq | opt199 |
| 30 | ![](https://smspva.com/templates/New_Design/images/ico/opt137_666304cb5c4b4.png "service-img") | bwin | opt137 |
| 31 | ![](https://smspva.com/templates/New_Design/images/ico/careem.png "service-img") | Careem | opt89 |
| 32 | ![](https://smspva.com/templates/New_Design/images/ico/opt255_6731d0f5bc67e.jpg "service-img") | Casa Pariurilor | opt255 |
| 33 | ![](https://smspva.com/templates/New_Design/images/ico/opt148_6663051dc7573.png "service-img") | casa.it | opt148 |
| 34 | ![](https://smspva.com/templates/New_Design/images/ico/opt226_6618e1e656bbe.png "service-img") | Cash App | opt226 |
| 35 | ![](https://smspva.com/templates/New_Design/images/ico/opt214_658020faa7c45.png "service-img") | Cashrewards | opt214 |
| 36 | ![](https://smspva.com/templates/New_Design/images/ico/opt201_657854eb0dc5e.jpg "service-img") | Casino Plus | opt201 |
| 37 | ![](https://smspva.com/templates/New_Design/images/ico/opt176_655c9e402576d.jpg "service-img") | ChoTot | opt176 |
| 38 | ![](https://smspva.com/templates/New_Design/images/ico/cmobil.ico "service-img") | CityMobil | opt76 |
| 39 | ![](https://smspva.com/templates/New_Design/images/ico/opt196_65703c0312d2f.png "service-img") | Claude (Anthropic) | opt196 |
| 40 | ![](https://smspva.com/templates/New_Design/images/ico/opt98_66630597a465a.png "service-img") | Clubhouse | opt98 |
| 41 | ![](https://smspva.com/templates/New_Design/images/ico/coinbase.png "service-img") | CoinBase | opt112 |
| 42 | ![](https://smspva.com/templates/New_Design/images/ico/contact.ico "service-img") | CONTACT | opt51 |
| 43 | ![](https://smspva.com/templates/New_Design/images/ico/craigslist.ico "service-img") | Craigslist | opt26 |
| 44 | ![](https://smspva.com/templates/New_Design/images/ico/opt124_666305f26e9d5.png "service-img") | Credit Karma | opt124 |
| 45 | ![](https://smspva.com/templates/New_Design/images/ico/opt157_65573a7277542.png "service-img") | CupidMedia | opt157 |
| 46 | ![](https://smspva.com/templates/New_Design/images/ico/opt150_66630661755a6.png "service-img") | Czech email services | opt150 |
| 47 | ![](https://smspva.com/templates/New_Design/images/ico/opt53_666306bc585f2.png "service-img") | Deliveroo | opt53 |
| 48 | ![](https://smspva.com/templates/New_Design/images/ico/opt204_65785f8da5185.png "service-img") | DenimApp | opt204 |
| 49 | ![](https://smspva.com/templates/New_Design/images/ico/didi.ico "service-img") | DiDi | opt92 |
| 50 | ![](https://smspva.com/templates/New_Design/images/ico/discord.ico "service-img") | Discord | opt45 |
| 51 | ![](https://smspva.com/templates/New_Design/images/ico/opt232_66277a123c10d.png "service-img") | DistroKid | opt232 |
| 52 | ![](https://smspva.com/templates/New_Design/images/ico/dodopizza.png "service-img") | Dodopizza + PapaJohns | opt27 |
| 53 | ![](https://smspva.com/templates/New_Design/images/ico/opt40_6663073ae9b40.png "service-img") | Doordash | opt40 |
| 54 | ![](https://smspva.com/templates/New_Design/images/ico/dromru.png "service-img") | Drom.RU | opt32 |
| 55 | ![](https://smspva.com/templates/New_Design/images/ico/drug.png "service-img") | Drug Vokrug | opt31 |
| 56 | ![](https://smspva.com/templates/New_Design/images/ico/opt136_666307d9f04d5.png "service-img") | dundle | opt136 |
| 57 | ![](https://smspva.com/templates/New_Design/images/ico/opt21_6663082ecc1bc.png "service-img") | EasyPay | opt21 |
| 58 | ![](https://smspva.com/templates/New_Design/images/ico/opt200_65785487ae8a7.jpg "service-img") | ENEBA | opt200 |
| 59 | ![](https://smspva.com/templates/New_Design/images/ico/opt248_66becf1d2c4fa.png "service-img") | ESX (abonamentesali.ro) | opt248 |
| 60 | ![](https://smspva.com/templates/New_Design/images/ico/opt141_6663088f13652.png "service-img") | EUROBET | opt141 |
| 61 | ![](https://smspva.com/templates/New_Design/images/ico/fb.png "service-img") | Facebook | opt2 |
| 62 | ![](https://smspva.com/templates/New_Design/images/ico/fastmail.png "service-img") | FastMail | opt43 |
| 63 | ![](https://smspva.com/templates/New_Design/images/ico/opt215_658023186e69f.png "service-img") | Fbet | opt215 |
| 64 | ![](https://smspva.com/templates/New_Design/images/ico/opt159_65573af945053.png "service-img") | Feeld | opt159 |
| 65 | ![](https://smspva.com/templates/New_Design/images/ico/opt6_666308f6e6723.png "service-img") | Fiverr | opt6 |
| 66 | ![](https://smspva.com/templates/New_Design/images/ico/opt139_666309490c426.png "service-img") | fontbet | opt139 |
| 67 | ![](https://smspva.com/templates/New_Design/images/ico/opt189_655ca5f13c9b3.png "service-img") | foodora | opt189 |
| 68 | ![](https://smspva.com/templates/New_Design/images/ico/foodpanda.png "service-img") | foodpanda | opt115 |
| 69 | ![](https://smspva.com/templates/New_Design/images/ico/opt221_65f2a3c9c749c.png "service-img") | Fortuna | opt221 |
| 70 | ![](https://smspva.com/templates/New_Design/images/ico/fotostrana.png "service-img") | Fotostrana | opt13 |
| 71 | ![](https://smspva.com/templates/New_Design/images/ico/opt142_6663098613401.png "service-img") | funpay | opt142 |
| 72 | ![](https://smspva.com/templates/New_Design/images/ico/g2a.jpg "service-img") | G2A.COM | opt68 |
| 73 | ![](https://smspva.com/templates/New_Design/images/ico/paxful.png "service-img") | Gameflip | opt77 |
| 74 | ![](https://smspva.com/templates/New_Design/images/ico/opt28_666309e76d144.png "service-img") | Gamers set (offgamers.com, G2A.com, seagm.com) | opt28 |
| 75 | ![](https://smspva.com/templates/New_Design/images/ico/opt179_655ca016d7361.png "service-img") | GetsBet.ro | opt179 |
| 76 | ![](https://smspva.com/templates/New_Design/images/ico/gettaxi.png "service-img") | GetTaxi | opt35 |
| 77 | ![](https://smspva.com/templates/New_Design/images/ico/opt188_655ca591689ef.png "service-img") | GGbet | opt188 |
| 78 | ![](https://smspva.com/templates/New_Design/images/ico/opt229_6627781a653e5.jpg "service-img") | GGPokerUK | opt229 |
| 79 | ![](https://smspva.com/templates/New_Design/images/ico/opt85_66630a3f4b444.png "service-img") | giocodigitale.it | opt85 |
| 80 | ![](https://smspva.com/templates/New_Design/images/ico/glovoraketa.ico "service-img") | Glovo & Raketa | opt108 |
| 81 | ![](https://smspva.com/templates/New_Design/images/ico/opt240_66879c1ad054d.jpg "service-img") | goldbet.it | opt240 |
| 82 | ![](https://smspva.com/templates/New_Design/images/ico/gmail.png "service-img") | Google (YouTube, Gmail) | opt1 |
| 83 | ![](https://smspva.com/templates/New_Design/images/ico/gmail.png "service-img") | Google Voice | opt140 |
| 84 | ![](https://smspva.com/templates/New_Design/images/ico/grabtaxi.png "service-img") | GrabTaxi | opt30 |
| 85 | ![](https://smspva.com/templates/New_Design/images/ico/grailed.png "service-img") | Grailed | opt420 |
| 86 | ![](https://smspva.com/templates/New_Design/images/ico/grindr.ico "service-img") | Grindr | opt110 |
| 87 | ![](https://smspva.com/templates/New_Design/images/ico/opt155_655716304f898.png "service-img") | Happn | opt155 |
| 88 | ![](https://smspva.com/templates/New_Design/images/ico/opt203_65785efc1689c.png "service-img") | HelloTalk | opt203 |
| 89 | ![](https://smspva.com/templates/New_Design/images/ico/opt238_667a2c8e7a580.png "service-img") | hepsiburada | opt238 |
| 90 | ![](https://smspva.com/templates/New_Design/images/ico/opt216_65a5f5900f846.png "service-img") | Hey | opt216 |
| 91 | ![](https://smspva.com/templates/New_Design/images/ico/opt120_66630aaf1328d.png "service-img") | Hinge | opt120 |
| 92 | ![](https://smspva.com/templates/New_Design/images/ico/opt144_66630aea202ae.png "service-img") | hopper | opt144 |
| 93 | ![](https://smspva.com/templates/New_Design/images/ico/opt166_6556153845310.png "service-img") | HUAWEI | opt166 |
| 94 | ![](https://smspva.com/templates/New_Design/images/ico/icard.png "service-img") | ICard | opt103 |
| 95 | ![](https://smspva.com/templates/New_Design/images/ico/opt165_66630b4899f30.png "service-img") | idealista.com | opt165 |
| 96 | ![](https://smspva.com/templates/New_Design/images/ico/opt55_66630b89aff92.png "service-img") | ifood | opt55 |
| 97 | ![](https://smspva.com/templates/New_Design/images/ico/imo.png "service-img") | IMO | opt111 |
| 98 | ![](https://smspva.com/templates/New_Design/images/ico/opt167_654de72ab4120.png "service-img") | inbox.lv | opt167 |
| 99 | ![](https://smspva.com/templates/New_Design/images/ico/inboxdollars.png "service-img") | Inboxdollars | opt118 |
| 100 | ![](https://smspva.com/templates/New_Design/images/ico/instagram.png "service-img") | Instagram (+Threads) | opt16 |
| 101 | ![](https://smspva.com/templates/New_Design/images/ico/opt193_65702a87b9141.png "service-img") | Ipsos | opt193 |
| 102 | ![](https://smspva.com/templates/New_Design/images/ico/opt243_6694df3aa6431.png "service-img") | IQOS | opt243 |
| 103 | ![](https://smspva.com/templates/New_Design/images/ico/jd.ico "service-img") | JD.com | opt94 |
| 104 | ![](https://smspva.com/templates/New_Design/images/ico/kakao.ico "service-img") | KakaoTalk | opt71 |
| 105 | ![](https://smspva.com/templates/New_Design/images/ico/opt175_655c995f936a3.png "service-img") | Klarna | opt175 |
| 106 | ![](https://smspva.com/templates/New_Design/images/ico/opt152_66630bd9c5aae.png "service-img") | kleinanzeigen.de | opt152 |
| 107 | ![](https://smspva.com/templates/New_Design/images/ico/opt99_66630c05209e0.png "service-img") | KoronaPay | opt99 |
| 108 | ![](https://smspva.com/templates/New_Design/images/ico/sbermarket.ico "service-img") | Kuper (SberMarket) | opt97 |
| 109 | ![](https://smspva.com/templates/New_Design/images/ico/kwiff.ico "service-img") | kwiff.com | opt129 |
| 110 | ![](https://smspva.com/templates/New_Design/images/ico/opt195_6570395fe0b3f.png "service-img") | Lajumate.ro | opt195 |
| 111 | ![](https://smspva.com/templates/New_Design/images/ico/opt180_655ca0b0de4b5.png "service-img") | Lalamove | opt180 |
| 112 | ![](https://smspva.com/templates/New_Design/images/ico/opt182_655ca1d5514bf.png "service-img") | LAPOSTE | opt182 |
| 113 | ![](https://smspva.com/templates/New_Design/images/ico/opt222_65f2a3fbe362f.jpg "service-img") | LASVEGAS.RO | opt222 |
| 114 | ![](https://smspva.com/templates/New_Design/images/ico/lazada.png "service-img") | Lazada | opt60 |
| 115 | ![](https://smspva.com/templates/New_Design/images/ico/opt164_65571a978d6e3.png "service-img") | Leboncoin | opt164 |
| 116 | ![](https://smspva.com/templates/New_Design/images/ico/line.ico "service-img") | Line Messenger | opt37 |
| 117 | ![](https://smspva.com/templates/New_Design/images/ico/linkedin.png "service-img") | LinkedIn | opt8 |
| 118 | ![](https://smspva.com/templates/New_Design/images/ico/opt245_66a453a3a5454.png "service-img") | Linode | opt245 |
| 119 | ![](https://smspva.com/templates/New_Design/images/ico/livescore.png "service-img") | LiveScore | opt42 |
| 120 | ![](https://smspva.com/templates/New_Design/images/ico/localbitcoins.png "service-img") | LocalBitcoins | opt105 |
| 121 | ![](https://smspva.com/templates/New_Design/images/ico/locanto.jpg "service-img") | Locanto.com | opt114 |
| 122 | ![](https://smspva.com/templates/New_Design/images/ico/lyft.ico "service-img") | Lyft | opt75 |
| 123 | ![](https://smspva.com/templates/New_Design/images/ico/opt126_66630c9094b53.png "service-img") | Magnit | opt126 |
| 124 | ![](https://smspva.com/templates/New_Design/images/ico/mail_black.png "service-img") | Mail.RU | opt33 |
| 125 | ![](https://smspva.com/templates/New_Design/images/ico/mailru.png "service-img") | Mail.ru Group | opt4 |
| 126 | ![](https://smspva.com/templates/New_Design/images/ico/mamba.ico "service-img") | Mamba | opt100 |
| 127 | ![](https://smspva.com/templates/New_Design/images/ico/opt171_6556077d514ef.jpg "service-img") | Marktplaats | opt171 |
| 128 | ![](https://smspva.com/templates/New_Design/images/ico/opt250_66e00cff34986.png "service-img") | Match | opt250 |
| 129 | ![](https://smspva.com/templates/New_Design/images/ico/opt219_65d85aacb2f0a.png "service-img") | maxline.by | opt219 |
| 130 | ![](https://smspva.com/templates/New_Design/images/ico/michat.png "service-img") | MiChat | opt96 |
| 131 | ![](https://smspva.com/templates/New_Design/images/ico/ms.png "service-img") | Microsoft (Azure, Bing, Skype, etc) | opt15 |
| 132 | ![](https://smspva.com/templates/New_Design/images/ico/opt156_655739cc1a3db.png "service-img") | mobileDE | opt156 |
| 133 | ![](https://smspva.com/templates/New_Design/images/ico/opt184_655ca302f1b2a.png "service-img") | MOMO | opt184 |
| 134 | ![](https://smspva.com/templates/New_Design/images/ico/monese.png "service-img") | Monese | opt121 |
| 135 | ![](https://smspva.com/templates/New_Design/images/ico/opt47_66630ce033c02.png "service-img") | MoneyLion | opt47 |
| 136 | ![](https://smspva.com/templates/New_Design/images/ico/opt254_67316d1b182a8.png "service-img") | Monster Energy | opt254 |
| 137 | ![](https://smspva.com/templates/New_Design/images/ico/opt197_65785390376e5.png "service-img") | MPSellers | opt197 |
| 138 | ![](https://smspva.com/templates/New_Design/images/ico/opt211_65801f33ea021.png "service-img") | MrGreen | opt211 |
| 139 | ![](https://smspva.com/templates/New_Design/images/ico/office365.ico "service-img") | MS Office 365 | opt7 |
| 140 | ![](https://smspva.com/templates/New_Design/images/ico/opt0_66630d21d0979.png "service-img") | myopinions & erewards | opt0 |
| 141 | ![](https://smspva.com/templates/New_Design/images/ico/naver.ico "service-img") | Naver | opt73 |
| 142 | ![](https://smspva.com/templates/New_Design/images/ico/opt198_657853fe74459.png "service-img") | Nectar | opt198 |
| 143 | ![](https://smspva.com/templates/New_Design/images/ico/netbet.ico "service-img") | NetBet | opt95 |
| 144 | ![](https://smspva.com/templates/New_Design/images/ico/neteller.ico "service-img") | Neteller | opt116 |
| 145 | ![](https://smspva.com/templates/New_Design/images/ico/netflix.ico "service-img") | Netflix | opt101 |
| 146 | ![](https://smspva.com/templates/New_Design/images/ico/opt202_65785e5c99854.jpg "service-img") | NHNCloud | opt202 |
| 147 | ![](https://smspva.com/templates/New_Design/images/ico/opt177_655c9ed951f22.png "service-img") | NHNcorp (강남언니) | opt177 |
| 148 | ![](https://smspva.com/templates/New_Design/images/ico/opt119_66630d716253d.png "service-img") | Nico | opt119 |
| 149 | ![](https://smspva.com/templates/New_Design/images/ico/opt151_66630d9ecbf7a.png "service-img") | novibet.com | opt151 |
| 150 | ![](https://smspva.com/templates/New_Design/images/ico/ok.png "service-img") | OD | opt5 |
| 151 | ![](https://smspva.com/templates/New_Design/images/ico/offerup.png "service-img") | OfferUp | opt113 |
| 152 | ![](https://smspva.com/templates/New_Design/images/ico/opt230_6627790906252.png "service-img") | OkCupid | opt230 |
| 153 | ![](https://smspva.com/templates/New_Design/images/ico/opt228_662776c65aa6f.png "service-img") | OKX | opt228 |
| 154 | ![](https://smspva.com/templates/New_Design/images/ico/olx.png "service-img") | OLX + goods.ru | opt70 |
| 155 | ![](https://smspva.com/templates/New_Design/images/ico/opt241_668b5cc59eed1.png "service-img") | onet.pl (Onet Konto) | opt241 |
| 156 | ![](https://smspva.com/templates/New_Design/images/ico/another.png "service-img") | OTHER (no guarantee) | opt19 |
| 157 | ![](https://smspva.com/templates/New_Design/images/ico/another.png "service-img") | OTHER (voice code) | opt00019 |
| 158 | ![](https://smspva.com/templates/New_Design/images/ico/opt212_65801fe22156e.png "service-img") | OurTime | opt212 |
| 159 | ![](https://smspva.com/templates/New_Design/images/ico/opt246_66a75c27314ca.jpg "service-img") | Outlier | opt246 |
| 160 | ![](https://smspva.com/templates/New_Design/images/ico/opt181_655ca17d51618.jpg "service-img") | OZON.ru | opt181 |
| 161 | ![](https://smspva.com/templates/New_Design/images/ico/paddypower.png "service-img") | Paddy Power | opt109 |
| 162 | ![](https://smspva.com/templates/New_Design/images/ico/opt169_65573ba54b8e3.png "service-img") | Pari.ru | opt169 |
| 163 | ![](https://smspva.com/templates/New_Design/images/ico/opt3_66630e40af702.png "service-img") | Parimatch | opt3 |
| 164 | ![](https://smspva.com/templates/New_Design/images/ico/opt162_655739fca1cbc.png "service-img") | Payoneer | opt162 |
| 165 | ![](https://smspva.com/templates/New_Design/images/ico/paypal.ico "service-img") | PayPal + Ebay | opt83 |
| 166 | ![](https://smspva.com/templates/New_Design/images/ico/opt122_66630e6507056.png "service-img") | Paysafecard | opt122 |
| 167 | ![](https://smspva.com/templates/New_Design/images/ico/opt183_655ca25582e36.png "service-img") | PAYSEND | opt183 |
| 168 | ![](https://smspva.com/templates/New_Design/images/ico/opt149_666315091b834.png "service-img") | pm.by | opt149 |
| 169 | ![](https://smspva.com/templates/New_Design/images/ico/pof.ico "service-img") | POF.com | opt84 |
| 170 | ![](https://smspva.com/templates/New_Design/images/ico/promua.ico "service-img") | Prom.UA | opt107 |
| 171 | ![](https://smspva.com/templates/New_Design/images/ico/protonmail.ico "service-img") | Proton Mail | opt57 |
| 172 | ![](https://smspva.com/templates/New_Design/images/ico/opt207_657860f02ca12.png "service-img") | Publi24 | opt207 |
| 173 | ![](https://smspva.com/templates/New_Design/images/ico/qiwi.png "service-img") | Qiwi | opt18 |
| 174 | ![](https://smspva.com/templates/New_Design/images/ico/opt247_66aaf3ff6e25b.png "service-img") | RadQuest | opt247 |
| 175 | ![](https://smspva.com/templates/New_Design/images/ico/opt154_65573c1d9ffef.png "service-img") | Rambler.ru | opt154 |
| 176 | ![](https://smspva.com/templates/New_Design/images/ico/opt133_6663154f63220.png "service-img") | Revolut | opt133 |
| 177 | ![](https://smspva.com/templates/New_Design/images/ico/opt153_65573b772b37d.png "service-img") | ROOMSTER | opt153 |
| 178 | ![](https://smspva.com/templates/New_Design/images/ico/opt170_65573bf46bb42.png "service-img") | Royal Canin | opt170 |
| 179 | ![](https://smspva.com/templates/New_Design/images/ico/opt186_655ca4149ac53.png "service-img") | RusDate | opt186 |
| 180 | ![](https://smspva.com/templates/New_Design/images/ico/opt185_655ca34cacf3f.png "service-img") | Samokat | opt185 |
| 181 | ![](https://smspva.com/templates/New_Design/images/ico/opt174_655c93471955e.png "service-img") | Samsung | opt174 |
| 182 | ![](https://smspva.com/templates/New_Design/images/ico/opt134_66631584e443d.png "service-img") | Schibsted-konto | opt134 |
| 183 | ![](https://smspva.com/templates/New_Design/images/ico/shopee.ico "service-img") | Shopee | opt48 |
| 184 | ![](https://smspva.com/templates/New_Design/images/ico/signal.png "service-img") | Signal | opt127 |
| 185 | ![](https://smspva.com/templates/New_Design/images/ico/opt38_666315d27fd60.png "service-img") | Sisal | opt38 |
| 186 | ![](https://smspva.com/templates/New_Design/images/ico/skout.png "service-img") | Skout | opt49 |
| 187 | ![](https://smspva.com/templates/New_Design/images/ico/skrill.ico "service-img") | Skrill | opt117 |
| 188 | ![](https://smspva.com/templates/New_Design/images/ico/snapchat.ico "service-img") | Snapchat | opt90 |
| 189 | ![](https://smspva.com/templates/New_Design/images/ico/opt190_66631618b8f0f.png "service-img") | SNKRDUNK | opt190 |
| 190 | ![](https://smspva.com/templates/New_Design/images/ico/opt234_66277c31c97c6.jpg "service-img") | Solitaire Cash | opt234 |
| 191 | ![](https://smspva.com/templates/New_Design/images/ico/steam.png "service-img") | Steam | opt58 |
| 192 | ![](https://smspva.com/templates/New_Design/images/ico/opt146_6663166e99628.png "service-img") | subito.it | opt146 |
| 193 | ![](https://smspva.com/templates/New_Design/images/ico/opt249_66cd532e50a46.jpg "service-img") | Superbet | opt249 |
| 194 | ![](https://smspva.com/templates/New_Design/images/ico/swagbucks.ico "service-img") | Swagbucks | opt125 |
| 195 | ![](https://smspva.com/templates/New_Design/images/ico/tango.jpg "service-img") | Tango | opt82 |
| 196 | ![](https://smspva.com/templates/New_Design/images/ico/opt161_65573bd0db8b8.jpg "service-img") | TANK.RU | opt161 |
| 197 | ![](https://smspva.com/templates/New_Design/images/ico/opt239_6686a402c737d.jpg "service-img") | Taptap | opt239 |
| 198 | ![](https://smspva.com/templates/New_Design/images/ico/taxi_maxim.png "service-img") | Taxi Maksim | opt74 |
| 199 | ![](https://smspva.com/templates/New_Design/images/ico/telegram.png "service-img") | Telegram | opt29 |
| 200 | ![](https://smspva.com/templates/New_Design/images/ico/telegram.png "service-img") | Telegram (voice code) | opt00029 |
| 201 | ![](https://smspva.com/templates/New_Design/images/ico/qq.png "service-img") | Tencent QQ | opt34 |
| 202 | ![](https://smspva.com/templates/New_Design/images/ico/ticketmaster.ico "service-img") | Ticketmaster | opt52 |
| 203 | ![](https://smspva.com/templates/New_Design/images/ico/tiktok.png "service-img") | TikTok | opt104 |
| 204 | ![](https://smspva.com/templates/New_Design/images/ico/tinder.png "service-img") | Tinder | opt9 |
| 205 | ![](https://smspva.com/templates/New_Design/images/ico/opt235_66277cfea7c12.png "service-img") | TLScontact | opt235 |
| 206 | ![](https://smspva.com/templates/New_Design/images/ico/opt191_656ef49a40563.jpg "service-img") | TopCashback | opt191 |
| 207 | ![](https://smspva.com/templates/New_Design/images/ico/opt220_65f2a39a0ebef.jpg "service-img") | TOTOGAMING | opt220 |
| 208 | ![](https://smspva.com/templates/New_Design/images/ico/opt218_65cdde639ba36.png "service-img") | TransferGo | opt218 |
| 209 | ![](https://smspva.com/templates/New_Design/images/ico/opt233_66277b08f3960.png "service-img") | TrueCaller | opt233 |
| 210 | ![](https://smspva.com/templates/New_Design/images/ico/opt244_6697a1805c2c2.png "service-img") | Truth Social | opt244 |
| 211 | ![](https://smspva.com/templates/New_Design/images/ico/twilio.png "service-img") | Twilio | opt66 |
| 212 | ![](https://smspva.com/templates/New_Design/images/ico/opt205_657860147869a.png "service-img") | Twitch | opt205 |
| 213 | ![](https://smspva.com/templates/New_Design/images/ico/opt160_65573ac5a1791.png "service-img") | U By Prodia | opt160 |
| 214 | ![](https://smspva.com/templates/New_Design/images/ico/uber.jpg "service-img") | Uber | opt72 |
| 215 | ![](https://smspva.com/templates/New_Design/images/ico/opt39_666316ca23ffd.png "service-img") | Verse | opt39 |
| 216 | ![](https://smspva.com/templates/New_Design/images/ico/viber.png "service-img") | Viber | opt11 |
| 217 | ![](https://smspva.com/templates/New_Design/images/ico/vinted.png "service-img") | Vinted | opt130 |
| 218 | ![](https://smspva.com/templates/New_Design/images/ico/vk_black.png "service-img") | VK (no guarantee) | opt69 |
| 219 | ![](https://smspva.com/templates/New_Design/images/ico/opt178_655c9fa709a13.png "service-img") | VonageVF | opt178 |
| 220 | ![](https://smspva.com/templates/New_Design/images/ico/opt147_6663171214afb.png "service-img") | VooV Meeting | opt147 |
| 221 | ![](https://smspva.com/templates/New_Design/images/ico/opt213_6580204be0c7e.jpg "service-img") | Waitomo | opt213 |
| 222 | ![](https://smspva.com/templates/New_Design/images/ico/opt206_65786091bfe43.png "service-img") | WalletHub | opt206 |
| 223 | ![](https://smspva.com/templates/New_Design/images/ico/opt227_66275f39aa809.png "service-img") | Walmart | opt227 |
| 224 | ![](https://smspva.com/templates/New_Design/images/ico/opt172_655c87eca1f10.png "service-img") | WEB.DE | opt172 |
| 225 | ![](https://smspva.com/templates/New_Design/images/ico/webmoney.png "service-img") | WebMoney&ENUM | opt24 |
| 226 | ![](https://smspva.com/templates/New_Design/images/ico/wechat.png "service-img") | WeChat | opt67 |
| 227 | ![](https://smspva.com/templates/New_Design/images/ico/weebly.png "service-img") | Weebly | opt54 |
| 228 | ![](https://smspva.com/templates/New_Design/images/ico/weststein.ico "service-img") | WESTSTEIN | opt80 |
| 229 | ![](https://smspva.com/templates/New_Design/images/ico/opt231_6627797fc0648.png "service-img") | Whatnot | opt231 |
| 230 | ![](https://smspva.com/templates/New_Design/images/ico/whatsapp.png "service-img") | WhatsAPP | opt20 |
| 231 | ![](https://smspva.com/templates/New_Design/images/ico/whatsapp.png "service-img") | WhatsAPP (voice code) | opt00020 |
| 232 | ![](https://smspva.com/templates/New_Design/images/ico/whoosh.ico "service-img") | Whoosh | opt123 |
| 233 | ![](https://smspva.com/templates/New_Design/images/ico/opt106_66631774989da.png "service-img") | Wing Money | opt106 |
| 234 | ![](https://smspva.com/templates/New_Design/images/ico/opt91_666317b2b934e.png "service-img") | Wise | opt91 |
| 235 | ![](https://smspva.com/templates/New_Design/images/ico/opt163_655607e9a3566.jpg "service-img") | Wolt | opt163 |
| 236 | ![](https://smspva.com/templates/New_Design/images/ico/opt208_6578614116272.png "service-img") | WooPlus | opt208 |
| 237 | ![](https://smspva.com/templates/New_Design/images/ico/twitter.png "service-img") | X (Twitter) | opt41 |
| 238 | ![](https://smspva.com/templates/New_Design/images/ico/opt173_655c907dc253f.png "service-img") | X World Wallet | opt173 |
| 239 | ![](https://smspva.com/templates/New_Design/images/ico/yahoo.png "service-img") | Yahoo | opt65 |
| 240 | ![](https://smspva.com/templates/New_Design/images/ico/yalla.png "service-img") | Yalla.live | opt88 |
| 241 | ![](https://smspva.com/templates/New_Design/images/ico/yandex.png "service-img") | Yandex&YooMoney | opt23 |
| 242 | ![](https://smspva.com/templates/New_Design/images/ico/opt236_66545076f0f9e.png "service-img") | Year13 | opt236 |
| 243 | ![](https://smspva.com/templates/New_Design/images/ico/opt158_65560834b69e9.png "service-img") | Zalo | opt158 |
| 244 | ![](https://smspva.com/templates/New_Design/images/ico/opt225_66068297c8f5e.png "service-img") | Zasilkovna | opt225 |
| 245 | ![](https://smspva.com/templates/New_Design/images/ico/zoho.png "service-img") | Zoho | opt93 |
| 246 | ![](https://smspva.com/templates/New_Design/images/ico/opt194_657030a853861.png "service-img") | ZoomInfo | opt194 |
| 247 | ![](https://smspva.com/templates/New_Design/images/ico/opt253_672c28e72b044.png "service-img") | Zoosk | opt253 |

[](https://docs.smspva.com/#tag/activation_v2_all_methods)All requests
======================================================================

[](https://docs.smspva.com/#tag/activation_v2_all_methods/paths/~1activation~1number~1{country}~1{service}/get)Get Number
-------------------------------------------------------------------------------------------------------------------------

Get a number for country and service

##### Authorizations:

*apikey*

##### path Parameters

| country

required

 |

string

Example: RU

Country 2 symbols name in ISO 3166-2 format, uppercase.\
[Countries list](https://docs.smspva.com/#tag/activation_v2_lists/Countries-list)

 |
| service

required

 |

string

Example: opt20

Service code.\
[Services list](https://docs.smspva.com/#tag/activation_v2_lists/Services-list)

 |

### Responses

**200**

Successful operation

##### Response Schema: application/json

| statusCode |

integer

Example: "200"

Result status code

 |
| data |

object

Response data

 |

**405**

Invalid parameters

**407**

Your balance is too low to receive sms for selected country and service.

**411**

API access limited by low karma or ratelimits

**500**

Failed to fetch number

**501**

Number not found

**502**

Number not found.

**503**

Server overload, try later.

get/activation/number/{country}/{service}

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url https://api.smspva.com/activation/number/RU/opt20\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200
-   405
-   407
-   411
-   500
-   501
-   502
-   503

Content type

application/json

Copy

Expand allCollapse all

`{

-   "statusCode": 200,

-   "data": {

    -   "orderId": 123456,

    -   "phoneNumber": 9876544321,

    -   "countryCode": "RU",

    -   "orderExpireIn": 600

    }

}`

[](https://docs.smspva.com/#tag/activation_v2_all_methods/paths/~1activation~1sms~1{orderid}/get)Receive SMS
------------------------------------------------------------------------------------------------------------

Receive SMS with service activation code

##### path Parameters

| orderid

required

 |

integer

Example: 123456

ID of order received in number response

 |

##### header Parameters

| partnerkey |

string

Example: 3eaa1c1f977d5a8152380f13cdfd03d0

Optional **partnerkey** parameter for referral system.

 |

### Responses

**200**

Successful operation

##### Response Schema: application/json

| statusCode |

integer

Example: "200"

Result status code

 |
| data |

object

Response data

 |

**202**

SMS not yet received

##### Response Schema: application/json

| statusCode |

integer

Example: "202"

Result status code

 |
| error |

object

Error data

 |

**405**

Invalid parameters

**406**

Order ID format is invalid or not found

**407**

We received SMS but your balance is not enough to pay it.

**410**

This order is closed and unavailable

**411**

API access limited by low karma or ratelimits

**500**

Failed to fetch SMS.

**501**

Server failed to process request.

**503**

The server is overloaded and experiencing performance issues. Please try later.

get/activation/sms/{orderid}

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url https://api.smspva.com/activation/sms/123456\
  --header 'partnerkey: SOME_STRING_VALUE'

### Response samples

-   200
-   202
-   405
-   406
-   407
-   410
-   411
-   500
-   501
-   503

Content type

application/json

Copy

Expand allCollapse all

`{

-   "statusCode": 200,

-   "data": {

    -   "sms": {},

    -   "orderId": "123456",

    -   "orderExpireIn": 600

    }

}`

[](https://docs.smspva.com/#tag/activation_v2_all_methods/paths/~1activation~1balance/get)Get user's balance
------------------------------------------------------------------------------------------------------------

Get user's balance

##### Authorizations:

*apikey*

### Responses

**200**

Successful operation

##### Response Schema: application/json

| statusCode |

integer

Example: "200"

Result status code

 |
| data |

object

Response data

 |

get/activation/balance

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url https://api.smspva.com/activation/balance\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "statusCode": 200,

-   "data": {

    -   "balance": 10.5

    }

}`

[](https://docs.smspva.com/#tag/activation_v2_all_methods/paths/~1activation~1userinfo/get)Get user's info
----------------------------------------------------------------------------------------------------------

Get user's info

##### Authorizations:

*apikey*

### Responses

**200**

Successful operation

##### Response Schema: application/json

| statusCode |

integer

Example: "200"

Result status code

 |
| data |

object

Response data

 |

get/activation/userinfo

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url https://api.smspva.com/activation/userinfo\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "statusCode": 200,

-   "data": {

    -   "balance": 10.5,

    -   "name": "user123",

    -   "karma": 100.5

    }

}`

[](https://docs.smspva.com/#tag/activation_v2_all_methods/paths/~1activation~1countnumbers~1{country}/get)Get available numbers count for each country and mobile operator
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Get available numbers count for each country and mobile operator

##### Authorizations:

*apikey*

##### path Parameters

| country |

string

Example: RU

Country 2 symbols name in ISO 3166-2 format, uppercase.\
[Countries list](https://docs.smspva.com/#tag/activation_v2_lists/Countries-list)

 |

### Responses

**200**

Successful operation

##### Response Schema: application/json

| statusCode |

integer

Example: "200"

Result status code

 |
| data |

Array of objects[ items ]

Response data

 |

get/activation/countnumbers/{country}

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url https://api.smspva.com/activation/countnumbers/RU\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "statusCode": 200,

-   "data": [

    -   []

    ]

}`

[](https://docs.smspva.com/#tag/activation_v2_all_methods/paths/~1activation~1serviceprice~1{country}~1{service}/get)Get service price specific country
-------------------------------------------------------------------------------------------------------------------------------------------------------

Get service price specific country

##### Authorizations:

*apikey*

##### path Parameters

| country

required

 |

string

Example: RU

Country 2 symbols name in ISO 3166-2 format, uppercase.\
[Countries list](https://docs.smspva.com/#tag/activation_v2_lists/Countries-list)

 |
| service

required

 |

string

Example: opt0

Service code.\
[Services list](https://docs.smspva.com/#tag/activation_v2_lists/Services-list)

 |

### Responses

**200**

Successful operation

##### Response Schema: application/json

| statusCode |

integer

Example: "200"

Result status code

 |
| data |

object

Response data

 |

get/activation/serviceprice/{country}/{service}

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url https://api.smspva.com/activation/serviceprice/RU/opt0\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "statusCode": 200,

-   "data": {

    -   "service": "opt0",

    -   "serviceDescription": "myopinions & erewards",

    -   "price": 0.5

    }

}`

[](https://docs.smspva.com/#tag/activation_v2_all_methods/paths/~1activation~1servicesprices/get)Get prices for all services
----------------------------------------------------------------------------------------------------------------------------

Get prices for all services

##### Authorizations:

*apikey*

### Responses

**200**

Successful operation

##### Response Schema: application/json

| statusCode |

integer

Example: "200"

Result status code

 |
| data |

Array of objects[ items ]

Response data

 |

get/activation/servicesprices

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url https://api.smspva.com/activation/servicesprices\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "statusCode": 200,

-   "data": [

    -   []

    ]

}`

[](https://docs.smspva.com/#tag/activation_v2_all_methods/paths/~1activation~1numberstatus~1{number}~1{service}/get)Check if number is still able to receive SMS for certain service
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Check if number is still able to receive SMS for certain service. Only if you used to receive SMS on this number for this service previously.

##### Authorizations:

*apikey*

##### path Parameters

| number

required

 |

integer

Example: 98765432

Phone number without country phone code.

 |
| service

required

 |

string

Example: opt0

Service code. To see all service codes please refer to servicesprices method.

 |

### Responses

**200**

Successful operation

##### Response Schema: application/json

| statusCode |

integer

Example: "200"

Result status code

 |
| data |

object

Response data

 |

**405**

Invalid number format

get/activation/numberstatus/{number}/{service}

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url https://api.smspva.com/activation/numberstatus/98765432/opt0\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200
-   405

Content type

application/json

Copy

Expand allCollapse all

`{

-   "statusCode": 200,

-   "data": {

    -   "number": 98765432,

    -   "orderId": 123456

    }

}`

[](https://docs.smspva.com/#tag/activation_v2_all_methods/paths/~1activation~1clearsms~1{orderid}/put)Delete current SMS to receive new one.
--------------------------------------------------------------------------------------------------------------------------------------------

Delete current SMS to receive new one.

##### Authorizations:

*apikey*

##### path Parameters

| orderid

required

 |

integer

Example: 123456

Order ID

 |

### Responses

**200**

Successful operation

##### Response Schema: application/json

| statusCode |

integer

Example: "200"

Result status code

 |
| data |

object

Response data

 |

**404**

No SMS received, or there's unpaid SMS waiting.

**405**

Invalid parameters

**406**

Order not found.

**501**

Server failed to process request.

**503**

No SMS received, or there's unpaid SMS waiting.

put/activation/clearsms/{orderid}

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request PUT\
  --url https://api.smspva.com/activation/clearsms/123456\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200
-   404
-   405
-   406
-   501
-   503

Content type

application/json

Copy

Expand allCollapse all

`{

-   "statusCode": 200,

-   "data": {

    -   "orderId": 123456,

    -   "orderExpireIn": 599

    }

}`

[](https://docs.smspva.com/#tag/activation_v2_all_methods/paths/~1activation~1cancelorder~1{orderid}/put)Cancel order.
----------------------------------------------------------------------------------------------------------------------

Cancel order.

##### Authorizations:

*apikey*

##### path Parameters

| orderid

required

 |

integer

Example: 123456

Order ID

 |

### Responses

**200**

Successful operation

##### Response Schema: application/json

| statusCode |

integer

Example: "200"

Result status code

 |
| data |

object

Response data

 |

**405**

Invalid parameters

**406**

Order ID format is invalid or not found

**411**

API access limited by low karma or ratelimits

**501**

Server failed to process request.

**503**

The server is overloaded and experiencing performance issues. Please try later.

put/activation/cancelorder/{orderid}

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request PUT\
  --url https://api.smspva.com/activation/cancelorder/123456\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200
-   405
-   406
-   411
-   501
-   503

Content type

application/json

Copy

Expand allCollapse all

`{

-   "statusCode": 200,

-   "data": {

    -   "orderId": 123456

    }

}`

[](https://docs.smspva.com/#tag/activation_v2_all_methods/paths/~1activation~1blocknumber~1{orderid}/put)Set number as nonworking.
----------------------------------------------------------------------------------------------------------------------------------

Set number as nonworking.

##### Authorizations:

*apikey*

##### path Parameters

| orderid

required

 |

integer

Example: 123456

Order ID

 |

### Responses

**200**

Successful operation

##### Response Schema: application/json

| statusCode |

integer

Example: "200"

Result status code

 |
| data |

object

Response data

 |

**405**

Invalid number format

**406**

Order ID format is invalid or not found

**411**

API access limited by low karma or ratelimits

**501**

Server failed to process request.

**503**

The server is overloaded and experiencing performance issues. Please try later.

put/activation/blocknumber/{orderid}

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request PUT\
  --url https://api.smspva.com/activation/blocknumber/123456\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200
-   405
-   406
-   411
-   501
-   503

Content type

application/json

Copy

Expand allCollapse all

`{

-   "statusCode": 200,

-   "data": {

    -   "orderId": 123456

    }

}`

[](https://docs.smspva.com/#tag/activation_v2_all_methods/paths/~1activation~1orders/get)Get current orders.
------------------------------------------------------------------------------------------------------------

Get current orders.

##### Authorizations:

*apikey*

### Responses

**200**

Successful operation

##### Response Schema: application/json

| statusCode |

integer

Example: "200"

Result status code

 |
| data |

object

Response data

 |

**501**

Server failed to process request.

**503**

The server is overloaded and experiencing performance issues. Please try later.

get/activation/orders

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url https://api.smspva.com/activation/orders\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200
-   501
-   503

Content type

application/json

Copy

Expand allCollapse all

`{

-   "statusCode": 200,

-   "data": {

    -   "orders": []

    }

}`

[](https://docs.smspva.com/#tag/rent_fast_start)Quick start
===========================================================

[](https://docs.smspva.com/#tag/rent_fast_start/operation/rent_create)Creating new order
----------------------------------------------------------------------------------------

Rent a number

##### query Parameters

| method

required

 |

string

Example: method=create

Method name

 |
| apikey

required

 |

string

Example: apikey=yourapikeyhere

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| dtype

required

 |

string

Example: dtype=week

Type of period: week or month

 |
| dcount

required

 |

integer

Example: dcount=1

Count type of period, i.e. if dtype=week then counts of weeks

 |
| country

required

 |

string

Example: country=RU

Country code of number\
[Countries list](https://docs.smspva.com/#tag/rent_lists/Countries-list)

 |
| service

required

 |

string

Example: service=opt6

Service code\
[Services list](https://docs.smspva.com/#tag/rent_lists/Services-list)

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Example: "1"

Status of the response: 1 for success, 0 for failure

 |
| data |

Array of objects

 |

get/api/rent.php?method=create

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=create&apikey=yourapikeyhere&dtype=week&dcount=1&country=RU&service=opt6'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "status": 1,

-   "data": [

    -   {}

    ]

}`

[](https://docs.smspva.com/#tag/rent_fast_start/operation/rent_create_multi)Сreating order with multiple services
-----------------------------------------------------------------------------------------------------------------

Rent a number

##### query Parameters

| method

required

 |

string

Example: method=create_multi

Method name

 |
| apikey

required

 |

string

Example: apikey=yourapikeyhere

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| dtype

required

 |

string

Example: dtype=week

Type of period: week or month

 |
| dcount

required

 |

integer

Example: dcount=1

Count type of period, i.e. if dtype=week then counts of weeks

 |
| country

required

 |

string

Example: country=RU

Country code of number\
[Countries list](https://docs.smspva.com/#tag/rent_lists/Countries-list)

 |
| services

required

 |

string

Example: services=opt6,opt7,opt8

Services codes separated by commas\
[Services list](https://docs.smspva.com/#tag/rent_lists/Services-list)

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Example: "1"

Status of the response: 1 for success, 0 for failure

 |
| data |

Array of objects

 |

get/api/rent.php?method=create_multi

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=create_multi&apikey=yourapikeyhere&dtype=week&dcount=1&country=RU&services=opt6%2Copt7%2Copt8'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "status": 1,

-   "data": [

    -   {}

    ]

}`

[](https://docs.smspva.com/#tag/rent_fast_start/operation/rent_activate)Activation phone number
-----------------------------------------------------------------------------------------------

Before sending an SMS, you must activate the number.

##### query Parameters

| method

required

 |

string

Example: method=activate

Method name

 |
| apikey

required

 |

string

Example: apikey=yourapikeyhere

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| id

required

 |

integer

Example: id=1

ID of order

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Example: "1"

Status of the response: 1 for success, 0 for failure

 |
| data |

Array of objects

 |

get/api/rent.php?method=activate

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=activate&apikey=yourapikeyhere&id=1'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "status": "1",

-   "data": [

    -   {}

    ]

}`

[](https://docs.smspva.com/#tag/rent_fast_start/operation/rent_orders)Getting list of orders
--------------------------------------------------------------------------------------------

Check the readiness to receive sms of the desired number

##### query Parameters

| method

required

 |

string

Example: method=orders

Method name

 |
| apikey

required

 |

string

Example: apikey=yourapikeyhere

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Example: "1"

Status of the response: 1 for success, 0 for failure

 |
| data |

Array of objects

 |

get/api/rent.php?method=orders

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=orders&apikey=yourapikeyhere'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "status": 1,

-   "data": [

    -   {}

    ]

}`

[](https://docs.smspva.com/#tag/rent_fast_start/operation/rent_sms)Getting all SMS of order
-------------------------------------------------------------------------------------------

Get SMS of number

##### query Parameters

| method

required

 |

string

Example: method=sms

Method name

 |
| apikey

required

 |

string

Example: apikey=yourapikeyhere

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| id

required

 |

integer

Example: id=123

ID of order

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Status of the response: 1 for success, 0 for failure

 |
| data |

Array of objects

 |

get/api/rent.php?method=sms

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=sms&apikey=yourapikeyhere&id=123'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "status": 0,

-   "data": [

    -   {}

    ]

}`

[](https://docs.smspva.com/#tag/rent_lists)Data list
====================================================

[](https://docs.smspva.com/#tag/rent_lists/Countries-list)Countries list
========================================================================

For select the country you need - indicate according country code at the "country" parameter.

| № | Flag | Country | Code |
| --- | --- | --- | --- |
| 1 | ![](https://smspva.com/templates/New_theme/images/flags/64/PR.png) | Puerto Rico | PR |
| 2 | ![](https://smspva.com/templates/New_theme/images/flags/64/US.png) | United States | US |
| 3 | ![](https://smspva.com/templates/New_theme/images/flags/64/CA.png) | Canada | CA |
| 4 | ![](https://smspva.com/templates/New_theme/images/flags/64/UK.png) | Unt. Kingdom | UK |
| 5 | ![](https://smspva.com/templates/New_theme/images/flags/64/FR.png) | France | FR |
| 6 | ![](https://smspva.com/templates/New_theme/images/flags/64/DE.png) | Germany | DE |
| 7 | ![](https://smspva.com/templates/New_theme/images/flags/64/IT.png) | Italy | IT |
| 8 | ![](https://smspva.com/templates/New_theme/images/flags/64/ES.png) | Spain | ES |
| 9 | ![](https://smspva.com/templates/New_theme/images/flags/64/AL.png) | Albania | AL |
| 10 | ![](https://smspva.com/templates/New_theme/images/flags/64/AR.png) | Argentina | AR |
| 11 | ![](https://smspva.com/templates/New_theme/images/flags/64/AU.png) | Australia | AU |
| 12 | ![](https://smspva.com/templates/New_theme/images/flags/64/AT.png) | Austria | AT |
| 13 | ![](https://smspva.com/templates/New_theme/images/flags/64/BD.png) | Bangladesh | BD |
| 14 | ![](https://smspva.com/templates/New_theme/images/flags/64/BG.png) | Bulgaria | BG |
| 15 | ![](https://smspva.com/templates/New_theme/images/flags/64/KH.png) | Cambodia | KH |
| 16 | ![](https://smspva.com/templates/New_theme/images/flags/64/HR.png) | Croatia | HR |
| 17 | ![](https://smspva.com/templates/New_theme/images/flags/64/CY.png) | Cyprus | CY |
| 18 | ![](https://smspva.com/templates/New_theme/images/flags/64/CZ.png) | Czech Republic | CZ |
| 19 | ![](https://smspva.com/templates/New_theme/images/flags/64/DK.png) | Denmark | DK |
| 20 | ![](https://smspva.com/templates/New_theme/images/flags/64/EG.png) | Egypt | EG |
| 21 | ![](https://smspva.com/templates/New_theme/images/flags/64/EE.png) | Estonia | EE |
| 22 | ![](https://smspva.com/templates/New_theme/images/flags/64/FI.png) | Finland | FI |
| 23 | ![](https://smspva.com/templates/New_theme/images/flags/64/GI.png) | Gibraltar | GI |
| 24 | ![](https://smspva.com/templates/New_theme/images/flags/64/GR.png) | Greece | GR |
| 25 | ![](https://smspva.com/templates/New_theme/images/flags/64/HK.png) | Hong Kong | HK |
| 26 | ![](https://smspva.com/templates/New_theme/images/flags/64/HU.png) | Hungary | HU |
| 27 | ![](https://smspva.com/templates/New_theme/images/flags/64/JP.png) | Japan | JP |
| 28 | ![](https://smspva.com/templates/New_theme/images/flags/64/MT.png) | Malta | MT |
| 29 | ![](https://smspva.com/templates/New_theme/images/flags/64/NO.png) | Norway | NO |
| 30 | ![](https://smspva.com/templates/New_theme/images/flags/64/CH.png) | Switzerland | CH |
| 31 | ![](https://smspva.com/templates/New_theme/images/flags/64/TZ.png) | Tanzania | TZ |
| 32 | ![](https://smspva.com/templates/New_theme/images/flags/64/ID.png) | Indonesia | ID |
| 33 | ![](https://smspva.com/templates/New_theme/images/flags/64/IE.png) | Ireland | IE |
| 34 | ![](https://smspva.com/templates/New_theme/images/flags/64/IL.png) | Israel | IL |
| 35 | ![](https://smspva.com/templates/New_theme/images/flags/64/KZ.png) | Kazakhstan | KZ |
| 36 | ![](https://smspva.com/templates/New_theme/images/flags/64/LV.png) | Latvia | LV |
| 37 | ![](https://smspva.com/templates/New_theme/images/flags/64/LT.png) | Lithuania | LT |
| 38 | ![](https://smspva.com/templates/New_theme/images/flags/64/MK.png) | Macedonia | MK |
| 39 | ![](https://smspva.com/templates/New_theme/images/flags/64/MY.png) | Malaysia | MY |
| 40 | ![](https://smspva.com/templates/New_theme/images/flags/64/MX.png) | Mexico | MX |
| 41 | ![](https://smspva.com/templates/New_theme/images/flags/64/MD.png) | Moldova | MD |
| 42 | ![](https://smspva.com/templates/New_theme/images/flags/64/NL.png) | Netherlands | NL |
| 43 | ![](https://smspva.com/templates/New_theme/images/flags/64/NZ.png) | New Zealand | NZ |
| 44 | ![](https://smspva.com/templates/New_theme/images/flags/64/PY.png) | Paraguay | PY |
| 45 | ![](https://smspva.com/templates/New_theme/images/flags/64/PH.png) | Philippines | PH |
| 46 | ![](https://smspva.com/templates/New_theme/images/flags/64/PL.png) | Poland | PL |
| 47 | ![](https://smspva.com/templates/New_theme/images/flags/64/PT.png) | Portugal | PT |
| 48 | ![](https://smspva.com/templates/New_theme/images/flags/64/RO.png) | Romania | RO |
| 49 | ![](https://smspva.com/templates/New_theme/images/flags/64/RU.png) | Russian Federation | RU |
| 50 | ![](https://smspva.com/templates/New_theme/images/flags/64/RS.png) | Serbia | RS |
| 51 | ![](https://smspva.com/templates/New_theme/images/flags/64/SK.png) | Slovakia | SK |
| 52 | ![](https://smspva.com/templates/New_theme/images/flags/64/SI.png) | Slovenia | SI |
| 53 | ![](https://smspva.com/templates/New_theme/images/flags/64/SE.png) | Sweden | SE |
| 54 | ![](https://smspva.com/templates/New_theme/images/flags/64/TH.png) | Thailand | TH |
| 55 | ![](https://smspva.com/templates/New_theme/images/flags/64/TR.png) | Turkey | TR |
| 56 | ![](https://smspva.com/templates/New_theme/images/flags/64/UA.png) | Ukraine | UA |

[](https://docs.smspva.com/#tag/rent_lists/Services-list)Services list
======================================================================

If you do not find the service you need, then you can use the OTHER (opt19) service or contact support to add the service you need.

| № | Logo | Service | Code |
| --- | --- | --- | --- |
| 1 | ![](https://smspva.com/templates/New_Design/images/ico/cupis_okcupid_winline.ico "service-img") | 1cupis & okcupid & winline | opt48 |
| 2 | ![](https://smspva.com/templates/New_Design/images/ico/opt77_6661c7608b541.png "service-img") | 1xbet | opt77 |
| 3 | ![](https://smspva.com/templates/New_Design/images/ico/airbnb.ico "service-img") | Airbnb (VRBO.com, HomeAway) | opt46 |
| 4 | ![](https://smspva.com/templates/New_Design/images/ico/opt204_667d171d8482e.jpg "service-img") | airtm | opt204 |
| 5 | ![](https://smspva.com/templates/New_Design/images/ico/another.png "service-img") | airwallex.com | opt161 |
| 6 | ![](https://smspva.com/templates/New_Design/images/ico/taobao.png "service-img") | Alibaba Group (TaoBao, AliPay, etc) | opt61 |
| 7 | ![](https://smspva.com/templates/New_Design/images/ico/amazon.ico "service-img") | Amazon | opt44 |
| 8 | ![](https://smspva.com/templates/New_Design/images/ico/apple.ico "service-img") | Apple | opt154 |
| 9 | ![](https://smspva.com/templates/New_Design/images/ico/opt206_667e39dab177b.jpg "service-img") | Ari10 | opt206 |
| 10 | ![](https://smspva.com/templates/New_Design/images/ico/astropay.png "service-img") | astropay.com | opt102 |
| 11 | ![](https://smspva.com/templates/New_Design/images/ico/avito.png "service-img") | Avito | opt59 |
| 12 | ![](https://smspva.com/templates/New_Design/images/ico/opt215_66c54910a3806.png "service-img") | B100 | opt215 |
| 13 | ![](https://smspva.com/templates/New_Design/images/ico/bankera.png "service-img") | bankera.com | opt45 |
| 14 | ![](https://smspva.com/templates/New_Design/images/ico/opt184_65ee7a5853d85.png "service-img") | Batery.in (baterybet) | opt184 |
| 15 | ![](https://smspva.com/templates/New_Design/images/ico/opt193_6629b53ad12c9.png "service-img") | Bazos.sk | opt193 |
| 16 | ![](https://smspva.com/templates/New_Design/images/ico/BBVA.svg "service-img") | BBVA | opt141 |
| 17 | ![](https://smspva.com/templates/New_Design/images/ico/bet365.png "service-img") | bet365 | opt43 |
| 18 | ![](https://smspva.com/templates/New_Design/images/ico/opt210_66a509d78ff78.png "service-img") | Betano | opt210 |
| 19 | ![](https://smspva.com/templates/New_Design/images/ico/betw.jpg "service-img") | betwinner3.com | opt51 |
| 20 | ![](https://smspva.com/templates/New_Design/images/ico/opt177_65bcb61b844d5.jpg "service-img") | Bilderlings | opt177 |
| 21 | ![](https://smspva.com/templates/New_Design/images/ico/binance.svg "service-img") | Binance | opt10 |
| 22 | ![](https://smspva.com/templates/New_Design/images/ico/opt203_6673e9b24d900.jpg "service-img") | bit2me | opt203 |
| 23 | ![](https://smspva.com/templates/New_Design/images/ico/opt207_668df78604984.png "service-img") | Bitnovo | opt207 |
| 24 | ![](https://smspva.com/templates/New_Design/images/ico/opt199_66617eaf02889.png "service-img") | Bitpanda | opt199 |
| 25 | ![](https://smspva.com/templates/New_Design/images/ico/BITSA.png "service-img") | BITSA | opt57 |
| 26 | ![](https://smspva.com/templates/New_Design/images/ico/opt94_6661c85dd2961.png "service-img") | Bitwala | opt94 |
| 27 | ![](https://smspva.com/templates/New_Design/images/ico/opt144_6661c9da72fb0.png "service-img") | blackcatcard | opt144 |
| 28 | ![](https://smspva.com/templates/New_Design/images/ico/blizzard.ico "service-img") | Blizzard(+battle.net) | opt3 |
| 29 | ![](https://smspva.com/templates/New_Design/images/ico/bluevine.jpeg "service-img") | bluevine | opt49 |
| 30 | ![](https://smspva.com/templates/New_Design/images/ico/Bnext.webp "service-img") | Bnext | opt25 |
| 31 | ![](https://smspva.com/templates/New_Design/images/ico/booking.svg "service-img") | booking | opt88 |
| 32 | ![](https://smspva.com/templates/New_Design/images/ico/opt214_66bed0f602dbd.png "service-img") | Bovada | opt214 |
| 33 | ![](https://smspva.com/templates/New_Design/images/ico/opt213_66ab489401712.jpg "service-img") | Brighty.app | opt213 |
| 34 | ![](https://smspva.com/templates/New_Design/images/ico/opt165_6661c91bc4e53.png "service-img") | Bumble.com | opt165 |
| 35 | ![](https://smspva.com/templates/New_Design/images/ico/BUNQ.png "service-img") | BUNQ | opt21 |
| 36 | ![](https://smspva.com/templates/New_Design/images/ico/another.png "service-img") | casa.it | opt98 |
| 37 | ![](https://smspva.com/templates/New_Design/images/ico/Chase.png "service-img") | Chase | opt40 |
| 38 | ![](https://smspva.com/templates/New_Design/images/ico/coinbase.svg "service-img") | CoinBase | opt70 |
| 39 | ![](https://smspva.com/templates/New_Design/images/ico/another.png "service-img") | CONTACT | opt164 |
| 40 | ![](https://smspva.com/templates/New_Design/images/ico/crypto-com.webp "service-img") | Crypto.com | opt56 |
| 41 | ![](https://smspva.com/templates/New_Design/images/ico/opt147_6661ca4081288.png "service-img") | Discord | opt147 |
| 42 | ![](https://smspva.com/templates/New_Design/images/ico/opt221_6721a31b81d9c.png "service-img") | DPD UK | opt221 |
| 43 | ![](https://smspva.com/templates/New_Design/images/ico/dukascopy.webp "service-img") | dukascopy | opt91 |
| 44 | ![](https://smspva.com/templates/New_Design/images/ico/Dzing.jpg "service-img") | Dzing | opt71 |
| 45 | ![](https://smspva.com/templates/New_Design/images/ico/opt194_664446f6b693a.png "service-img") | Esselunga | opt194 |
| 46 | ![](https://smspva.com/templates/New_Design/images/ico/eurobet.jpg "service-img") | EUROBET | opt68 |
| 47 | ![](https://smspva.com/templates/New_Design/images/ico/fb.png "service-img") | Facebook | opt2 |
| 48 | ![](https://smspva.com/templates/New_Design/images/ico/opt171_657aab7b2e129.png "service-img") | Fbet | opt171 |
| 49 | ![](https://smspva.com/templates/New_Design/images/ico/opt179_65cddcccd90c4.png "service-img") | Finom | opt179 |
| 50 | ![](https://smspva.com/templates/New_Design/images/ico/fiverr.svg "service-img") | Fiverr | opt6 |
| 51 | ![](https://smspva.com/templates/New_Design/images/ico/opt181_65e6d0b537b87.jpg "service-img") | Flowbank | opt181 |
| 52 | ![](https://smspva.com/templates/New_Design/images/ico/fonbet.jpg "service-img") | fonbet | opt158 |
| 53 | ![](https://smspva.com/templates/New_Design/images/ico/opt190_661e203cb14c2.png "service-img") | Foxpay | opt190 |
| 54 | ![](https://smspva.com/templates/New_Design/images/ico/og.png "service-img") | gemini.com | opt54 |
| 55 | ![](https://smspva.com/templates/New_Design/images/ico/gmail.png "service-img") | Google (GMail, YTube, etc.) | opt1 |
| 56 | ![](https://smspva.com/templates/New_Design/images/ico/opt220_670766b1dad60.png "service-img") | Green Dot | opt220 |
| 57 | ![](https://smspva.com/templates/New_Design/images/ico/guavapay.jpeg "service-img") | Guavapay(+Myguava) | opt152 |
| 58 | ![](https://smspva.com/templates/New_Design/images/ico/opt185_65eed27c27e70.png "service-img") | Hinge | opt185 |
| 59 | ![](https://smspva.com/templates/New_Design/images/ico/holvi.ico "service-img") | Holvi | opt80 |
| 60 | ![](https://smspva.com/templates/New_Design/images/ico/huobi.png "service-img") | huobi.com | opt150 |
| 61 | ![](https://smspva.com/templates/New_Design//images/ico/another.png "service-img") | hype.it | opt105 |
| 62 | ![](https://smspva.com/templates/New_Design/images/ico/iCard.png "service-img") | iCard | opt99 |
| 63 | ![](https://smspva.com/templates/New_Design/images/ico/imagin.png "service-img") | imagin | opt89 |
| 64 | ![](https://smspva.com/templates/New_Design/images/ico/indeed.png "service-img") | Indeed.com | opt34 |
| 65 | ![](https://smspva.com/templates/New_Design/images/ico/opt174_65b8b1104f060.png "service-img") | ing (.es, .it, etc) | opt174 |
| 66 | ![](https://smspva.com/templates/New_Design/images/ico/instagram.png "service-img") | Instagram (+Threads) | opt16 |
| 67 | ![](https://smspva.com/templates/New_Design/images/ico/opt198_665e983e24d32.png "service-img") | JD.com | opt198 |
| 68 | ![](https://smspva.com/templates/New_Design/images/ico/Joust2trade.jpg "service-img") | Joust2trade | opt92 |
| 69 | ![](https://smspva.com/templates/New_Design/images/ico/opt201_66728e2fa127e.png "service-img") | KCEX | opt201 |
| 70 | ![](https://smspva.com/templates/New_Design/images/ico/opt156_6661ca8c2b040.png "service-img") | Klarna | opt156 |
| 71 | ![](https://smspva.com/templates/New_Design/images/ico/opt178_65c34de195327.png "service-img") | Kleinanzeigen | opt178 |
| 72 | ![](https://smspva.com/templates/New_Design/images/ico/Kraken.svg "service-img") | Kraken | opt81 |
| 73 | ![](https://smspva.com/templates/New_Design/images/ico/opt166_6661cb07b86b5.png "service-img") | kucoin/bybit | opt166 |
| 74 | ![](https://smspva.com/templates/New_Design/images/ico/opt216_66c7e1b9b7464.png "service-img") | Leboncoin | opt216 |
| 75 | ![](https://smspva.com/templates/New_Design/images/ico/opt187_660baeba94ffe.png "service-img") | libero.it | opt187 |
| 76 | ![](https://smspva.com/templates/New_Design/images/ico/opt32_6661cb44c8f8a.png "service-img") | LINE | opt32 |
| 77 | ![](https://smspva.com/templates/New_Design/images/ico/linkedin.png "service-img") | LinkedIn | opt8 |
| 78 | ![](https://smspva.com/templates/New_Design/images/ico/opt175_65b8b13809766.png "service-img") | Lottomatica.it (Better, Goldbet, Betflag) | opt175 |
| 79 | ![](https://smspva.com/templates/New_Design/images/ico/opt167_6661cbbb1af9f.png "service-img") | Lydia(+Sumeria) | opt167 |
| 80 | ![](https://smspva.com/templates/New_Design/images/ico/mailru.png "service-img") | Mail.RU (VK, OK, Youla) | opt33 |
| 81 | ![](https://smspva.com/templates/New_Design/images/ico/mailru.png "service-img") | Mail.ru Group | opt4 |
| 82 | ![](https://smspva.com/templates/New_Design/images/ico/opt96_6661cc19385ee.png "service-img") | match.com | opt96 |
| 83 | ![](https://smspva.com/templates/New_Design/images/ico/Microsoft.ico "service-img") | Microsoft (Azure, Bing, HotMail, etc.) | opt15 |
| 84 | ![](https://smspva.com/templates/New_Design/images/ico/opt222_672b32ad3c0ac.png "service-img") | mobileDE | opt222 |
| 85 | ![](https://smspva.com/templates/New_Design/images/ico/pb.ico "service-img") | Monese | opt97 |
| 86 | ![](https://smspva.com/templates/New_Design/images/ico/moneygram.jpg "service-img") | moneygram.com | opt35 |
| 87 | ![](https://smspva.com/templates/New_Design/images/ico/Moneyjar.png "service-img") | Moneyjar | opt140 |
| 88 | ![](https://smspva.com/templates/New_Design/images/ico/moneyL.jpg "service-img") | MoneyLion | opt75 |
| 89 | ![](https://smspva.com/templates/New_Design/images/ico/another.png "service-img") | Moneytopay | opt162 |
| 90 | ![](https://smspva.com/templates/New_Design/images/ico/opt183_65eada1202f39.png "service-img") | mooneygroup.it | opt183 |
| 91 | ![](https://smspva.com/templates/New_Design/images/ico/opt143_6661cc6b0cec8.png "service-img") | Mostbet | opt143 |
| 92 | ![](https://smspva.com/templates/New_Design/images/ico/opt191_661e202d61dd4.png "service-img") | MyBookie | opt191 |
| 93 | ![](https://smspva.com/templates/New_Design/images/ico/opt168_65573cf02d6c9.png "service-img") | myfin.bg | opt168 |
| 94 | ![](https://smspva.com/templates/New_Design/images/ico/N26.png "service-img") | N26 | opt52 |
| 95 | ![](https://smspva.com/templates/New_Design/images/ico/opt186_6603e9ed924f9.png "service-img") | NamirialTSP | opt186 |
| 96 | ![](https://smspva.com/templates/New_Design/images/ico/opt211_66a61c2da0d45.png "service-img") | NCSOFT | opt211 |
| 97 | ![](https://smspva.com/templates/New_Design/images/ico/neteller.svg "service-img") | Neteller | opt1001 |
| 98 | ![](https://smspva.com/templates/New_Design/images/ico/nexo.svg "service-img") | nexo.io | opt26 |
| 99 | ![](https://smspva.com/templates/New_Design/images/ico/opt189_6613785c9b9e3.png "service-img") | nickel.eu | opt189 |
| 100 | ![](https://smspva.com/templates/New_Design/images/ico/opt197_665e97e6effd2.png "service-img") | Noelse | opt197 |
| 101 | ![](https://smspva.com/templates/New_Design/images/ico/northone.png "service-img") | northone.com | opt30 |
| 102 | ![](https://smspva.com/templates/New_Design/images/ico/okx.png "service-img") | okx.com | opt95 |
| 103 | ![](https://smspva.com/templates/New_Design/images/ico/openbank.png "service-img") | openbank.es | opt13 |
| 104 | ![](https://smspva.com/templates/New_Design/images/ico/oo-icon-192.png "service-img") | opinionoutpost | opt28 |
| 105 | ![](https://smspva.com/templates/New_Design/images/ico/another.png "service-img") | OTHER | opt142 |
| 106 | ![](https://smspva.com/templates/New_Design/images/ico/opt27_6661ccc06b7f0.png "service-img") | ourtime.com | opt27 |
| 107 | ![](https://smspva.com/templates/New_Design/images/ico/opt217_66ce7c9c949a1.jpg "service-img") | Outlier | opt217 |
| 108 | ![](https://smspva.com/templates/New_Design/images/ico/opt148_6661cd1a35377.png "service-img") | OZON.ru | opt148 |
| 109 | ![](https://smspva.com/templates/New_Design/images/ico/paxful.png "service-img") | Paxful (Noone) | opt72 |
| 110 | ![](https://smspva.com/templates/New_Design/images/ico/payoneer.svg "service-img") | Payoneer | opt103 |
| 111 | ![](https://smspva.com/templates/New_Design/images/ico/paypal.ico "service-img") | PayPal + Ebay | opt83 |
| 112 | ![](https://smspva.com/templates/New_Design/images/ico/Paysafecard.png "service-img") | Paysafecard (+Mojeplatnosci) | opt90 |
| 113 | ![](https://smspva.com/templates/New_Design/images/ico/PaySend.png "service-img") | PaySend | opt38 |
| 114 | ![](https://smspva.com/templates/New_Design/images/ico/opt172_65815b7a40d54.png "service-img") | Paysera | opt172 |
| 115 | ![](https://smspva.com/templates/New_Design/images/ico/opt159_6661cd5765256.png "service-img") | paytend | opt159 |
| 116 | ![](https://smspva.com/templates/New_Design/images/ico/opt205_667e2fb36afb0.png "service-img") | Payz | opt205 |
| 117 | ![](https://smspva.com/templates/New_Design/images/ico/opt195_66470d1c4d2f5.png "service-img") | Payzy | opt195 |
| 118 | ![](https://smspva.com/templates/New_Design/images/ico/opt196_66470e07df0d3.png "service-img") | Payzy | opt196 |
| 119 | ![](https://smspva.com/templates/New_Design/images/ico/opt202_6673e3c57d392.png "service-img") | pecunpay | opt202 |
| 120 | ![](https://smspva.com/templates/New_Design/images/ico/opt93_6661cdac24741.png "service-img") | Phyre | opt93 |
| 121 | ![](https://smspva.com/templates/New_Design/images/ico/another.png "service-img") | plazo.es | opt145 |
| 122 | ![](https://smspva.com/templates/New_Design/images/ico/pockit.png "service-img") | pockit | opt157 |
| 123 | ![](https://smspva.com/templates/New_Design/images/ico/pof.png "service-img") | POF | opt84 |
| 124 | ![](https://smspva.com/templates/New_Design/images/ico/vksurfing.png "service-img") | Pointsbet&Betmgm&Chime&Schwab | opt37 |
| 125 | ![](https://smspva.com/templates/New_Design/images/ico/pyypl.png "service-img") | Pyypl | opt42 |
| 126 | ![](https://smspva.com/templates/New_Design/images/ico/qiwi.png "service-img") | Qiwi | opt18 |
| 127 | ![](https://smspva.com/templates/New_Design/images/ico/opt170_657aab5f2afc4.png "service-img") | Qonto | opt170 |
| 128 | ![](https://smspva.com/templates/New_Design/images/ico/Rebellion.png "service-img") | Rebellion | opt73 |
| 129 | ![](https://smspva.com/templates/New_Design/images/ico/opt218_66eed242f1133.png "service-img") | Rebet.com | opt218 |
| 130 | ![](https://smspva.com/templates/New_Design/images/ico/opt208_66a3796060fed.png "service-img") | RedotPay | opt208 |
| 131 | ![](https://smspva.com/templates/New_Design/images/ico/relayfi.png "service-img") | relayfi.com | opt53 |
| 132 | ![](https://smspva.com/templates/New_Design/images/ico/Revolut.svg "service-img") | Revolut | opt101 |
| 133 | ![](https://smspva.com/templates/New_Design/images/ico/opt219_66f50a5886615.png "service-img") | REWARDCARD | opt219 |
| 134 | ![](https://smspva.com/templates/New_Design/images/ico/opt60_6661cde0e70a4.png "service-img") | riamoneytransfer | opt60 |
| 135 | ![](https://smspva.com/templates/New_Design/images/ico/opt176_65b8b14f195df.png "service-img") | shine.fr | opt176 |
| 136 | ![](https://smspva.com/templates/New_Design/images/ico/signal.png "service-img") | Signal | opt153 |
| 137 | ![](https://smspva.com/templates/New_Design/images/ico/sisal.jpg "service-img") | sisal | opt155 |
| 138 | ![](https://smspva.com/templates/New_Design/images/ico/skrill.ico "service-img") | Skrill | opt74 |
| 139 | ![](https://smspva.com/templates/New_Design/images/ico/steam.png "service-img") | Steam | opt58 |
| 140 | ![](https://smspva.com/templates/New_Design/images/ico/opt182_65e930f09a719.png "service-img") | SumUp | opt182 |
| 141 | ![](https://smspva.com/templates/New_Design/images/ico/opt173_65850f14e0ef8.png "service-img") | Swagbucks | opt173 |
| 142 | ![](https://smspva.com/templates/New_Design/images/ico/opt188_661376cec3147.png "service-img") | swissmoney | opt188 |
| 143 | ![](https://smspva.com/templates/New_Design/images/ico/opt212_66a855982bba8.png "service-img") | Taptap | opt212 |
| 144 | ![](https://smspva.com/templates/New_Design/images/ico/telegram.png "service-img") | Telegram | opt29 |
| 145 | ![](https://smspva.com/templates/New_Design/images/ico/opt209_66a506ce4d732.png "service-img") | Tic Life | opt209 |
| 146 | ![](https://smspva.com/templates/New_Design/images/ico/ticM.png "service-img") | Ticketmaster | opt146 |
| 147 | ![](https://smspva.com/templates/New_Design/images/ico/tiktok.png "service-img") | TikTok | opt104 |
| 148 | ![](https://smspva.com/templates/New_Design/images/ico/tinder.png "service-img") | Tinder | opt9 |
| 149 | ![](https://smspva.com/templates/New_Design/images/ico/opt180_65cddcdc2cf23.png "service-img") | Transfego | opt180 |
| 150 | ![](https://smspva.com/templates/New_Design/images/ico/opt160_6661ce3009036.png "service-img") | trastra.com | opt160 |
| 151 | ![](https://smspva.com/templates/New_Design/images/ico/twilio.png "service-img") | Twilio & eToro | opt66 |
| 152 | ![](https://smspva.com/templates/New_Design/images/ico/popular-topic-128.ico "service-img") | ValuedOpinions | opt39 |
| 153 | ![](https://smspva.com/templates/New_Design/images/ico/venmo.svg "service-img") | Venmo | opt85 |
| 154 | ![](https://smspva.com/templates/New_Design/images/ico/Verse.webp "service-img") | Verse | opt17 |
| 155 | ![](https://smspva.com/templates/New_Design/images/ico/opt200_66690641e1d86.jpg "service-img") | VFS Global application | opt200 |
| 156 | ![](https://smspva.com/templates/New_Design/images/ico/viber.png "service-img") | Viber | opt11 |
| 157 | ![](https://smspva.com/templates/New_Design/images/ico/vinted.png "service-img") | Vinted | opt31 |
| 158 | ![](https://smspva.com/templates/New_Design/images/ico/unnamed.webp "service-img") | Vivastreet | opt67 |
| 159 | ![](https://smspva.com/templates/New_Design/images/ico/Vivid.png "service-img") | Vivid | opt100 |
| 160 | ![](https://smspva.com/templates/New_Design/images/ico/Symbol_Black.svg "service-img") | Volet(Advcash) | opt78 |
| 161 | ![](https://smspva.com/templates/New_Design/images/ico/opt169_6566d70fd0b58.png "service-img") | VRBO.com | opt169 |
| 162 | ![](https://smspva.com/templates/New_Design/images/ico/wallester.ico "service-img") | wallester.com | opt149 |
| 163 | ![](https://smspva.com/templates/New_Design/images/ico/opt192_661e2f20e90b6.png "service-img") | Walmart | opt192 |
| 164 | ![](https://smspva.com/templates/New_Design/images/ico/webmoney.png "service-img") | WebMoney&ENUM | opt24 |
| 165 | ![](https://smspva.com/templates/New_Design/images/ico/worldcore.ico "service-img") | westernunion | opt82 |
| 166 | ![](https://smspva.com/templates/New_Design/images/ico/weststein.ico "service-img") | Weststein(MasterCard) | opt76 |
| 167 | ![](https://smspva.com/templates/New_Design/images/ico/whatsapp.png "service-img") | WhatsAPP | opt20 |
| 168 | ![](https://smspva.com/templates/New_Design/images/ico/another.png "service-img") | Willhaben | opt163 |
| 169 | ![](https://smspva.com/templates/New_Design/images/ico/Wirex.png "service-img") | Wirex | opt7 |
| 170 | ![](https://smspva.com/templates/New_Design/images/ico/wise.webp "service-img") | Wise (TransferWise) | opt0 |
| 171 | ![](https://smspva.com/templates/New_Design/images/ico/twitter.png "service-img") | X (Twitter) | opt41 |
| 172 | ![](https://smspva.com/templates/New_Design/images/ico/social_yahoo.png "service-img") | Yahoo | opt65 |
| 173 | ![](https://smspva.com/templates/New_Design/images/ico/yandex.png "service-img") | Yandex&YooMoney | opt23 |
| 174 | ![](https://smspva.com/templates/New_Design/images/ico/zen.svg "service-img") | zen | opt151 |

[](https://docs.smspva.com/#tag/rent_all_methods)All requests
=============================================================

[](https://docs.smspva.com/#tag/rent_all_methods/operation/rent_create)Creating new order
-----------------------------------------------------------------------------------------

Rent a number

##### query Parameters

| method

required

 |

string

Example: method=create

Method name

 |
| apikey

required

 |

string

Example: apikey=yourapikeyhere

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| dtype

required

 |

string

Example: dtype=week

Type of period: week or month

 |
| dcount

required

 |

integer

Example: dcount=1

Count type of period, i.e. if dtype=week then counts of weeks

 |
| country

required

 |

string

Example: country=RU

Country code of number\
[Countries list](https://docs.smspva.com/#tag/rent_lists/Countries-list)

 |
| service

required

 |

string

Example: service=opt6

Service code\
[Services list](https://docs.smspva.com/#tag/rent_lists/Services-list)

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Example: "1"

Status of the response: 1 for success, 0 for failure

 |
| data |

Array of objects

 |

get/api/rent.php?method=create

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=create&apikey=yourapikeyhere&dtype=week&dcount=1&country=RU&service=opt6'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "status": 1,

-   "data": [

    -   {}

    ]

}`

[](https://docs.smspva.com/#tag/rent_all_methods/operation/rent_create_multi)Сreating order with multiple services
------------------------------------------------------------------------------------------------------------------

Rent a number

##### query Parameters

| method

required

 |

string

Example: method=create_multi

Method name

 |
| apikey

required

 |

string

Example: apikey=yourapikeyhere

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| dtype

required

 |

string

Example: dtype=week

Type of period: week or month

 |
| dcount

required

 |

integer

Example: dcount=1

Count type of period, i.e. if dtype=week then counts of weeks

 |
| country

required

 |

string

Example: country=RU

Country code of number\
[Countries list](https://docs.smspva.com/#tag/rent_lists/Countries-list)

 |
| services

required

 |

string

Example: services=opt6,opt7,opt8

Services codes separated by commas\
[Services list](https://docs.smspva.com/#tag/rent_lists/Services-list)

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Example: "1"

Status of the response: 1 for success, 0 for failure

 |
| data |

Array of objects

 |

get/api/rent.php?method=create_multi

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=create_multi&apikey=yourapikeyhere&dtype=week&dcount=1&country=RU&services=opt6%2Copt7%2Copt8'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "status": 1,

-   "data": [

    -   {}

    ]

}`

[](https://docs.smspva.com/#tag/rent_all_methods/operation/rent_activate)Activation phone number
------------------------------------------------------------------------------------------------

Before sending an SMS, you must activate the number.

##### query Parameters

| method

required

 |

string

Example: method=activate

Method name

 |
| apikey

required

 |

string

Example: apikey=yourapikeyhere

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| id

required

 |

integer

Example: id=1

ID of order

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Example: "1"

Status of the response: 1 for success, 0 for failure

 |
| data |

Array of objects

 |

get/api/rent.php?method=activate

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=activate&apikey=yourapikeyhere&id=1'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "status": "1",

-   "data": [

    -   {}

    ]

}`

[](https://docs.smspva.com/#tag/rent_all_methods/operation/rent_orders)Getting list of orders
---------------------------------------------------------------------------------------------

Check the readiness to receive sms of the desired number

##### query Parameters

| method

required

 |

string

Example: method=orders

Method name

 |
| apikey

required

 |

string

Example: apikey=yourapikeyhere

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Example: "1"

Status of the response: 1 for success, 0 for failure

 |
| data |

Array of objects

 |

get/api/rent.php?method=orders

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=orders&apikey=yourapikeyhere'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "status": 1,

-   "data": [

    -   {}

    ]

}`

[](https://docs.smspva.com/#tag/rent_all_methods/operation/rent_sms)Getting all SMS of order
--------------------------------------------------------------------------------------------

Get SMS of number

##### query Parameters

| method

required

 |

string

Example: method=sms

Method name

 |
| apikey

required

 |

string

Example: apikey=yourapikeyhere

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| id

required

 |

integer

Example: id=123

ID of order

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Status of the response: 1 for success, 0 for failure

 |
| data |

Array of objects

 |

get/api/rent.php?method=sms

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=sms&apikey=yourapikeyhere&id=123'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "status": 0,

-   "data": [

    -   {}

    ]

}`

[](https://docs.smspva.com/#tag/rent_all_methods/operation/rent_getcountries)Getting available countries list
-------------------------------------------------------------------------------------------------------------

Get available countries list

##### query Parameters

| method

required

 |

string

Example: method=getcountries

Method name

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

 |
| data |

Array of objects

 |

get/api/rent.php?method=getcountries

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=getcountries'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "status": 0,

-   "data": [

    -   {}

    ]

}`

[](https://docs.smspva.com/#tag/rent_all_methods/operation/rent_getdata)Getting available services list
-------------------------------------------------------------------------------------------------------

Get a list of available services

##### query Parameters

| method

required

 |

string

Example: method=getdata

Method name

 |
| apikey

required

 |

string

Example: apikey=yourapikeyhere

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| country

required

 |

string

Example: country=RU

Country code of number\
[Countries list](https://docs.smspva.com/#tag/rent_lists/Countries-list)

 |
| dtype

required

 |

string

Example: dtype=week

Type of period: week or month

 |
| dcount

required

 |

integer

Example: dcount=1

Count type of period, i.e. if dtype=week then counts of weeks

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Status of the response: 1 for success, 0 for failure

 |
| data |

Array of objects

 |

get/api/rent.php?method=getdata

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=getdata&apikey=yourapikeyhere&country=RU&dtype=week&dcount=1'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "status": 0,

-   "data": [

    -   {}

    ]

}`

[](https://docs.smspva.com/#tag/rent_all_methods/operation/rent_add_service_to_order)Adding new service for existing order
--------------------------------------------------------------------------------------------------------------------------

Add another service to order

##### query Parameters

| method

required

 |

string

Example: method=add_service_to_order

Method name

 |
| apikey

required

 |

string

Example: apikey=yourapikeyhere

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| id

required

 |

integer

Example: id=56547

ID of order

 |
| service

required

 |

string

Example: service=opt89

Service code\
[Services list](https://docs.smspva.com/#tag/rent_lists/Services-list)

 |
| pnumber

required

 |

string

Example: pnumber=79335445295

rented phone number with country code without plus sign

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Example: "1"

Status of the response: 1 for success, 0 for failure

 |

get/api/rent.php?method=add_service_to_order

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=add_service_to_order&apikey=yourapikeyhere&id=56547&service=opt89&pnumber=79335445295'

### Response samples

-   200

Content type

application/json

Copy

`{

-   "status": 1

}`

[](https://docs.smspva.com/#tag/rent_all_methods/operation/rent_prolong)Prolongation order
------------------------------------------------------------------------------------------

Prolongation

##### query Parameters

| method

required

 |

string

Example: method=prolong

Method name

 |
| apikey

required

 |

string

Example: apikey=yourapikeyhere

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| id

required

 |

integer

Example: id=123

ID of order

 |
| dtype

required

 |

string

Example: dtype=week

Type of period: week or month

 |
| dcount

required

 |

integer

Example: dcount=1

Count type of period, i.e. if dtype=week then counts of weeks

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Status of the response: 1 for success, 0 for failure

 |
| data |

object

 |

get/api/rent.php?method=prolong

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=prolong&apikey=yourapikeyhere&id=123&dtype=week&dcount=1'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "status": 0,

-   "data": {

    -   "id": "123"

    }

}`

[](https://docs.smspva.com/#tag/rent_all_methods/operation/rent_delete)Removing order
-------------------------------------------------------------------------------------

Removing

##### query Parameters

| method

required

 |

string

Example: method=delete

Method name

 |
| apikey

required

 |

string

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| id |

integer

ID of order

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Example: "1"

Status of the response: 1 for success, 0 for failure

 |
| data |

object

 |

get/api/rent.php?method=delete

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=delete&apikey=SOME_STRING_VALUE&id=SOME_INTEGER_VALUE'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "status": 1,

-   "data": {

    -   "id": 123

    }

}`

[](https://docs.smspva.com/#tag/rent_all_methods/operation/rent_get_rent_history)Getting history of rental
----------------------------------------------------------------------------------------------------------

To restore the lease agreement, you need to get the order ID. To get a list of orders with the necessary information from the archive, you can request

##### query Parameters

| method

required

 |

string

Example: method=get_rent_history

Method name

 |
| apikey

required

 |

string

Example: apikey=yourapikeyhere

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| skip |

integer

Example: skip=0

Number of items to skip

 |
| take |

integer

Example: take=10

Number of items received

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Example: "1"

Status of the response: 1 for success, 0 for failure

 |
| data |

Array of objects

 |

get/api/rent.php?method=get_rent_history

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=get_rent_history&apikey=yourapikeyhere&skip=0&take=10'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "status": 1,

-   "data": [

    -   {}

    ]

}`

[](https://docs.smspva.com/#tag/rent_all_methods/operation/rent_restore_user_precalc)Precalcution of restoring
--------------------------------------------------------------------------------------------------------------

After receiving the ID of the desired reservation, you need to make another request to check the availability of the for rent`s and calculate the cost of restoration.

##### query Parameters

| method

required

 |

string

Example: method=restore_user_precalc

Method name

 |
| apikey

required

 |

string

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| id |

integer

ID of order

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Status of the response: 1 for success, 0 for failure

 |
| data |

object

 |

get/api/rent.php?method=restore_user_precalc

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=restore_user_precalc&apikey=SOME_STRING_VALUE&id=SOME_INTEGER_VALUE'

### Response samples

-   200

Content type

application/json

Copy

Expand allCollapse all

`{

-   "status": 0,

-   "data": {

    -   "ccode": "EN",

    -   "scode": "opt59",

    -   "price": 2.4,

    -   "sname": "Avito",

    -   "pnumber": "79929831844",

    -   "outdays": 32,

    -   "orderid": 317017,

    -   "prolongTo": 30

    }

}`

[](https://docs.smspva.com/#tag/rent_all_methods/operation/rent_restore_user)Restoring of outdated order
--------------------------------------------------------------------------------------------------------

If an exception occurs, we will receive a status with the value 0 and an error message in the msg field. at the bottom of the instructions is a list of possible exceptions and their description\
After receiving a positive response and agreeing to the terms of the lease restoration, you can make a last request that will return the rental number\
The request will return an object with status and data fields, if the values are positive, then the number has been restored. If the values are not positive, double-check the data and try again, if this also did not help, contact the site support service

##### query Parameters

| method

required

 |

string

Example: method=restore_user

Method name

 |
| apikey

required

 |

string

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| id |

integer

ID of order

 |

### Responses

**200**

Success

##### Response Schema: application/json

| status |

integer

Example: "1"

Status of the response: 1 for success, 0 for failure

 |
| data |

boolean

Example: "true"

Boolean indicating if the number has been restored

 |

get/api/rent.php?method=restore_user

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/api/rent.php?method=restore_user&apikey=SOME_STRING_VALUE&id=SOME_INTEGER_VALUE'

### Response samples

-   200

Content type

application/json

Copy

`{

-   "status": 1,

-   "data": true

}`

[](https://docs.smspva.com/#tag/activation_alternative_fast_start)Quick start
=============================================================================

[](https://docs.smspva.com/#tag/activation_alternative_fast_start/paths/~1stubs~1handler_api.php?action=getNumber/get)Getting phone number
------------------------------------------------------------------------------------------------------------------------------------------

Getting phone number

##### query Parameters

| action

required

 |

string

Example: action=getnumber

 |
| api_key

required

 |

string

Example: api_key=yourapikeyhere

 |
| country

required

 |

string

Example: country=0

Country code\
[Countries list](https://docs.smspva.com/#tag/activation_alternative_lists/Countries-list)

 |
| service

required

 |

string

Example: service=go

Service code\
[Services list](https://docs.smspva.com/#tag/activation_alternative_lists/Services-list)

 |
| operator |

string

Example: operator=MTS_RU

 |

### Responses

**200**

Successfully response

##### Response Schema: text/plain

One of 

Phone number receivedNo available phone numbers

string (Phone number received)

ACCESS_NUMBER:ORDERID:PHONENUMBER

get/stubs/handler_api.php?action=getNumber

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/stubs/handler_api.php?action=getNumber&api_key=yourapikeyhere&country=0&service=go&operator=MTS_RU'

[](https://docs.smspva.com/#tag/activation_alternative_fast_start/paths/~1stubs~1handler_api.php?action=getstatus/get)Getting SMS
---------------------------------------------------------------------------------------------------------------------------------

Getting SMS

##### query Parameters

| action

required

 |

string

Example: action=getstatus

Action type

 |
| api_key

required

 |

string

Example: api_key=yourapikeyhere

User's APIKEY

 |
| id

required

 |

string

Example: id=123

Order id

 |

### Responses

**200**

Successfully response

##### Response Schema: text/plain

One of 

Success. SMS receivedError. Bad apikeyError. Order not found or ID exists

string (Success. SMS received)

STATUS_OK:SMS TEXT HERE

get/stubs/handler_api.php?action=getstatus

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/stubs/handler_api.php?action=getstatus&api_key=yourapikeyhere&id=123'

[](https://docs.smspva.com/#tag/activation_alternative_lists)Data list
======================================================================

[](https://docs.smspva.com/#tag/activation_alternative_lists/Countries-list)Countries list
==========================================================================================

| Alternative's code | SMSPVA's code |
| --- | --- |
| 0 | RU |
| 1 | UA |
| 2 | KZ |
| 3 | CN2 |
| 4 | PH |
| 5 | GE |
| 6 | ID |
| 7 | BY |
| 8 | KE |
| 10 | VN |
| 11 | KG |
| 12 | US |
| 13 | IL |
| 14 | PY |
| 15 | PL |
| 16 | UK |
| 17 | US3 |
| 18 | FI |
| 20 | MO |
| 21 | EG |
| 22 | IN |
| 23 | IE |
| 24 | KH |
| 26 | HT |
| 27 | CI |
| 28 | GM |
| 29 | RS |
| 30 | YE |
| 31 | ZA |
| 32 | RO |
| 33 | SE |
| 34 | EE |
| 38 | GH |
| 39 | AR |
| 42 | TD |
| 43 | DE |
| 44 | LT |
| 48 | NL |
| 49 | LV |
| 51 | BY |
| 56 | ES |
| 63 | CZ |
| 67 | NZ |
| 68 | GN |
| 69 | ML |
| 73 | BR |
| 117 | PT |
| 78 | FR |
| 172 | DK |
| 85 | MD |
| 86 | CO |

[](https://docs.smspva.com/#tag/activation_alternative_lists/Services-list)Services list
========================================================================================

| Alternative's code | SMSPVA's code |
| --- | --- |
| vk | opt69 |
| mg | opt4 |
| ok | opt5 |
| wa | opt20 |
| vi | opt11 |
| tg | opt29 |
| wb | opt67 |
| go | opt1 |
| av | opt59 |
| fb | opt2 |
| tw | opt41 |
| ot | opt19 |
| ub | opt72 |
| qw | opt18 |
| gt | opt35 |
| sn | opt70 |
| ig | opt16 |
| ym | opt14 |
| ma | opt33 |
| mm | opt15 |
| uk | opt46 |
| me | opt37 |
| mb | opt65 |
| we | opt31 |
| bd | opt102 |
| kp | opt47 |
| ya | opt23 |
| mt | opt58 |
| oi | opt9 |
| fd | opt17 |
| zz | opt99 |
| kt | opt71 |
| pm | opt10 |
| tn | opt8 |
| tiktok | opt104 |
| mi | opt106 |
| mts | opt48 |
| rsa | opt111 |
| magnit | opt106 |
| ry | opt118 |
| yf | opt76 |
| re | opt112 |
| ab | opt61 |
| am | opt44 |
| tx | opt81 |
| pd | opt55 |
| dp | opt57 |
| hz | opt32 |
| kc | opt130 |
| qj | opt123 |
| xj | opt97 |

[](https://docs.smspva.com/#tag/activation_alternative_all_methods)All requests
===============================================================================

[](https://docs.smspva.com/#tag/activation_alternative_all_methods/paths/~1stubs~1handler_api.php?action=getNumber/get)Getting phone number
-------------------------------------------------------------------------------------------------------------------------------------------

Getting phone number

##### query Parameters

| action

required

 |

string

Example: action=getnumber

 |
| api_key

required

 |

string

Example: api_key=yourapikeyhere

 |
| country

required

 |

string

Example: country=0

Country code\
[Countries list](https://docs.smspva.com/#tag/activation_alternative_lists/Countries-list)

 |
| service

required

 |

string

Example: service=go

Service code\
[Services list](https://docs.smspva.com/#tag/activation_alternative_lists/Services-list)

 |
| operator |

string

Example: operator=MTS_RU

 |

### Responses

**200**

Successfully response

##### Response Schema: text/plain

One of 

Phone number receivedNo available phone numbers

string (Phone number received)

ACCESS_NUMBER:ORDERID:PHONENUMBER

get/stubs/handler_api.php?action=getNumber

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/stubs/handler_api.php?action=getNumber&api_key=yourapikeyhere&country=0&service=go&operator=MTS_RU'

[](https://docs.smspva.com/#tag/activation_alternative_all_methods/paths/~1stubs~1handler_api.php?action=getbalance/get)Getting user's balance
----------------------------------------------------------------------------------------------------------------------------------------------

Getting user's balance

##### query Parameters

| action

required

 |

string

Example: action=getbalance

 |
| api_key

required

 |

string

Example: api_key=yourapikeyhere

 |

### Responses

**200**

Successfully response

##### Response Schema: text/plain

One of 

SuccessError. Bad apikey

string (Success)

ACCESS_BALANCE:BALANCE VALUE HERE

get/stubs/handler_api.php?action=getbalance

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/stubs/handler_api.php?action=getbalance&api_key=yourapikeyhere'

[](https://docs.smspva.com/#tag/activation_alternative_all_methods/paths/~1stubs~1handler_api.php?action=setstatus&status=8/get)Close order
-------------------------------------------------------------------------------------------------------------------------------------------

Close order

##### query Parameters

| action

required

 |

string

Example: action=setstatus

 |
| api_key

required

 |

string

Example: api_key=yourapikeyhere

 |
| status

required

 |

string

Example: status=-1

Status which need to set

 |
| id

required

 |

string

Example: id=123

Order ID

 |

### Responses

**200**

Successfully response

##### Response Schema: text/plain

One of 

Order successfully cancelledError. Bad apikey

string (Order successfully cancelled)

ACCESS_CANCEL

get/stubs/handler_api.php?action=setstatus&status=8

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/stubs/handler_api.php?action=setstatus&api_key=yourapikeyhere&status=8&id=123'

[](https://docs.smspva.com/#tag/activation_alternative_all_methods/paths/~1stubs~1handler_api.php?action=setstatus&status=-1/get)Cancel order
---------------------------------------------------------------------------------------------------------------------------------------------

Cancel order

##### query Parameters

| action

required

 |

string

Example: action=setstatus

 |
| api_key

required

 |

string

Example: api_key=yourapikeyhere

 |
| status

required

 |

string

Example: status=-1

Status which need to set

 |
| id

required

 |

string

Example: id=123

Order ID

 |

### Responses

**200**

Successfully response

##### Response Schema: text/plain

One of 

Order successfully cancelledError. Bad apikey

string (Order successfully cancelled)

ACCESS_CANCEL

get/stubs/handler_api.php?action=setstatus&status=-1

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/stubs/handler_api.php?action=setstatus&api_key=yourapikeyhere&status=-1&id=123'

[](https://docs.smspva.com/#tag/activation_alternative_all_methods/paths/~1stubs~1handler_api.php?action=setstatus&status=6/get)Closing order
---------------------------------------------------------------------------------------------------------------------------------------------

Closing order

##### query Parameters

| action

required

 |

string

Example: action=setstatus

Action type

 |
| api_key

required

 |

string

Example: api_key=yourapikeyhere

User's APIKEY

 |
| id

required

 |

string

Example: id=123

Order id

 |

### Responses

**200**

Successfully response

##### Response Schema: text/plain

One of 

Success. SMS receivedError. Bad apikeyError. Order not found or ID exists

string (Success. SMS received)

STATUS_OK:SMS TEXT HERE

get/stubs/handler_api.php?action=setstatus&status=6

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/stubs/handler_api.php?action=setstatus&api_key=yourapikeyhere&id=123&status=6'

[](https://docs.smspva.com/#tag/activation_alternative_all_methods/paths/~1stubs~1handler_api.php?action=getstatus/get)Getting SMS
----------------------------------------------------------------------------------------------------------------------------------

Getting SMS

##### query Parameters

| action

required

 |

string

Example: action=getstatus

Action type

 |
| api_key

required

 |

string

Example: api_key=yourapikeyhere

User's APIKEY

 |
| id

required

 |

string

Example: id=123

Order id

 |

### Responses

**200**

Successfully response

##### Response Schema: text/plain

One of 

Success. SMS receivedError. Bad apikeyError. Order not found or ID exists

string (Success. SMS received)

STATUS_OK:SMS TEXT HERE

get/stubs/handler_api.php?action=getstatus

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/stubs/handler_api.php?action=getstatus&api_key=yourapikeyhere&id=123'

[](https://docs.smspva.com/#tag/activation_alternative_errors)Errors
====================================================================

BAD_ACTION - Incorrect action parameter\
ERROR_SQL - Technical error on server\
BAD_KEY - Incorrect APIKEY parameter\
NO_ACTIVATION - Order not found or expired\
BAD_STATUS - Incorrect status parameter

[](https://docs.smspva.com/#tag/activation_fast_start)Quick start
=================================================================

[](https://docs.smspva.com/#tag/activation_fast_start/operation/getUserByName)Getting phone number
--------------------------------------------------------------------------------------------------

Request for receiving a phone number for a certain service

##### Authorizations:

*apikey*

#####  API Key: apikey

**Header parameter name: **`apikey`

##### query Parameters

| apikey

required

 |

string

Example: apikey=DSWAFvdedrE4

Your API key

 |
| service

required

 |

string

Example: service=opt4

Service code

 |
| country

required

 |

string

Example: country=RU

Country code

 |
| metod

required

 |

string

Example: metod=get_number

Method name

 |

### Responses

**200**

Success

##### Response Schema: application/json

| response |

string

Example: "2"

Status

 |
| number |

string

Example: "9871234567"

Number to receive SMS

 |
| id |

string

Example: "25623"

Order ID

 |

get/priemnik.php?method=get_number

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/priemnik.php?apikey=DSWAFvdedrE4&service=opt4&country=RU&metod=get_number&method=get_number'\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Copy

`{

-   "response": "2",

-   "number": "9871234567",

-   "id": "25623"

}`

[](https://docs.smspva.com/#tag/activation_fast_start/operation/get_sms)Getting SMS
-----------------------------------------------------------------------------------

Receiving an SMS for a certain service\
In this method id parameter is indicated from the response to request for phone number get_number

> **Note**\
>\
> If you get the response that a code from SMS hasn't been found yet, send request get_sms once again 20 seconds later. Note, the server searches for SMS for 10 minutes. You need to send your request within 10 minutes each 20 seconds per one request. That said, you receive a code from SMS or error message.\
**Code Refinement**\
If you want to get re-SMS without closing the order (Code Refinement), then just on the method get_sms add additional parameter sms=sms Example string:

 https://smspva.com/priemnik.php?\
 metod=get_sms\
 &country=ru\
 &service=opt4\
 &id=25623\
 &apikey=DSWAFvdedrE4\
 &sms=sms\
In this case, your order can not be closed and you may receive a re-SMS. Re-chargeable SMS. The cost is the cost of an ordinary SMS for this service.

##### Authorizations:

*apikey*

##### query Parameters

| apikey

required

 |

string

Example: apikey=DSWAFvdedrE4

Your API key

 |
| service

required

 |

string

Example: service=opt4

Service code

 |
| country

required

 |

string

Example: country=RU

Country code

 |
| id

required

 |

string

Example: id=3421

ID of the order

 |
| metod

required

 |

string

Example: metod=get_sms

Method name

 |

### Responses

**200**

Success

##### Response Schema: application/json

| response |

string

Example: "2"

Status

 |
| number |

string

Example: "9871234567"

Number to receive SMS

 |
| sms |

string

Example: "234562"

Code from SMS

 |

get/priemnik.php?method=get_sms

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/priemnik.php?apikey=DSWAFvdedrE4&service=opt4&country=RU&id=3421&metod=get_sms&method=get_sms'\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Copy

`{

-   "response": 2,

-   "number": "9871234567",

-   "sms": "234562"

}`

[](https://docs.smspva.com/#tag/activation_v2_lists)Data list
=============================================================

[](https://docs.smspva.com/#tag/activation_v2_lists/Countries-list)Countries list
=================================================================================

For select the country you need - indicate according country code at the "country" parameter.

| № | Flag | Country | Code |
| --- | --- | --- | --- |
| 1 | ![](https://smspva.com/templates/New_theme/images/flags/64/US.png) | United States | US |
| 2 | ![](https://smspva.com/templates/New_theme/images/flags/64/CA.png) | Canada | CA |
| 3 | ![](https://smspva.com/templates/New_theme/images/flags/64/UK.png) | Unt. Kingdom | UK |
| 4 | ![](https://smspva.com/templates/New_theme/images/flags/64/FR.png) | France | FR |
| 5 | ![](https://smspva.com/templates/New_theme/images/flags/64/DE.png) | Germany | DE |
| 6 | ![](https://smspva.com/templates/New_theme/images/flags/64/IT.png) | Italy | IT |
| 7 | ![](https://smspva.com/templates/New_theme/images/flags/64/ES.png) | Spain | ES |
| 8 | ![](https://smspva.com/templates/New_theme/images/flags/64/AL.png) | Albania | AL |
| 9 | ![](https://smspva.com/templates/New_theme/images/flags/64/AR.png) | Argentina | AR |
| 10 | ![](https://smspva.com/templates/New_theme/images/flags/64/AU.png) | Australia | AU |
| 11 | ![](https://smspva.com/templates/New_theme/images/flags/64/AT.png) | Austria | AT |
| 12 | ![](https://smspva.com/templates/New_theme/images/flags/64/BD.png) | Bangladesh | BD |
| 13 | ![](https://smspva.com/templates/New_theme/images/flags/64/BA.png) | Bos. and Herz. | BA |
| 14 | ![](https://smspva.com/templates/New_theme/images/flags/64/BR.png) | Brazil | BR |
| 15 | ![](https://smspva.com/templates/New_theme/images/flags/64/BG.png) | Bulgaria | BG |
| 16 | ![](https://smspva.com/templates/New_theme/images/flags/64/KH.png) | Cambodia | KH |
| 17 | ![](https://smspva.com/templates/New_theme/images/flags/64/CM.png) | Cameroon | CM |
| 18 | ![](https://smspva.com/templates/New_theme/images/flags/64/CL.png) | Chile | CL |
| 19 | ![](https://smspva.com/templates/New_theme/images/flags/64/CO.png) | Colombia | CO |
| 20 | ![](https://smspva.com/templates/New_theme/images/flags/64/HR.png) | Croatia | HR |
| 21 | ![](https://smspva.com/templates/New_theme/images/flags/64/CY.png) | Cyprus | CY |
| 22 | ![](https://smspva.com/templates/New_theme/images/flags/64/CZ.png) | Czech Republic | CZ |
| 23 | ![](https://smspva.com/templates/New_theme/images/flags/64/DK.png) | Denmark | DK |
| 24 | ![](https://smspva.com/templates/New_theme/images/flags/64/DO.png) | Dominicana | DO |
| 25 | ![](https://smspva.com/templates/New_theme/images/flags/64/EG.png) | Egypt | EG |
| 26 | ![](https://smspva.com/templates/New_theme/images/flags/64/EE.png) | Estonia | EE |
| 27 | ![](https://smspva.com/templates/New_theme/images/flags/64/FI.png) | Finland | FI |
| 28 | ![](https://smspva.com/templates/New_theme/images/flags/64/GE.png) | Georgia | GE |
| 29 | ![](https://smspva.com/templates/New_theme/images/flags/64/GH.png) | Ghana (Virtual) | GH |
| 30 | ![](https://smspva.com/templates/New_theme/images/flags/64/GI.png) | Gibraltar | GI |
| 31 | ![](https://smspva.com/templates/New_theme/images/flags/64/GR.png) | Greece | GR |
| 32 | ![](https://smspva.com/templates/New_theme/images/flags/64/HK.png) | Hong Kong | HK |
| 33 | ![](https://smspva.com/templates/New_theme/images/flags/64/HU.png) | Hungary | HU |
| 34 | ![](https://smspva.com/templates/New_theme/images/flags/64/IN.png) | India | IN |
| 35 | ![](https://smspva.com/templates/New_theme/images/flags/64/JP.png) | Japan | JP |
| 36 | ![](https://smspva.com/templates/New_theme/images/flags/64/KG.png) | Kyrgyzstan (Virtual) | KG |
| 37 | ![](https://smspva.com/templates/New_theme/images/flags/64/MT.png) | Malta | MT |
| 38 | ![](https://smspva.com/templates/New_theme/images/flags/64/NO.png) | Norway | NO |
| 39 | ![](https://smspva.com/templates/New_theme/images/flags/64/PK.png) | Pakistan (Virtual) | PK |
| 40 | ![](https://smspva.com/templates/New_theme/images/flags/64/SA.png) | Saudi Arabia | SA |
| 41 | ![](https://smspva.com/templates/New_theme/images/flags/64/SG.png) | Singapore | SG |
| 42 | ![](https://smspva.com/templates/New_theme/images/flags/64/CH.png) | Switzerland | CH |
| 43 | ![](https://smspva.com/templates/New_theme/images/flags/64/TZ.png) | Tanzania | TZ |
| 44 | ![](https://smspva.com/templates/New_theme/images/flags/64/UZ.png) | Uzbekistan (Virtual) | UZ |
| 45 | ![](https://smspva.com/templates/New_theme/images/flags/64/ID.png) | Indonesia | ID |
| 46 | ![](https://smspva.com/templates/New_theme/images/flags/64/IE.png) | Ireland | IE |
| 47 | ![](https://smspva.com/templates/New_theme/images/flags/64/IL.png) | Israel | IL |
| 48 | ![](https://smspva.com/templates/New_theme/images/flags/64/KZ.png) | Kazakhstan | KZ |
| 49 | ![](https://smspva.com/templates/New_theme/images/flags/64/KE.png) | Kenya | KE |
| 50 | ![](https://smspva.com/templates/New_theme/images/flags/64/LA.png) | Laos | LA |
| 51 | ![](https://smspva.com/templates/New_theme/images/flags/64/LV.png) | Latvia | LV |
| 52 | ![](https://smspva.com/templates/New_theme/images/flags/64/LT.png) | Lithuania | LT |
| 53 | ![](https://smspva.com/templates/New_theme/images/flags/64/MK.png) | Macedonia | MK |
| 54 | ![](https://smspva.com/templates/New_theme/images/flags/64/MY.png) | Malaysia | MY |
| 55 | ![](https://smspva.com/templates/New_theme/images/flags/64/MX.png) | Mexico | MX |
| 56 | ![](https://smspva.com/templates/New_theme/images/flags/64/MD.png) | Moldova | MD |
| 57 | ![](https://smspva.com/templates/New_theme/images/flags/64/MA.png) | Morocco | MA |
| 58 | ![](https://smspva.com/templates/New_theme/images/flags/64/NL.png) | Netherlands | NL |
| 59 | ![](https://smspva.com/templates/New_theme/images/flags/64/NZ.png) | New Zealand | NZ |
| 60 | ![](https://smspva.com/templates/New_theme/images/flags/64/NG.png) | Nigeria | NG |
| 61 | ![](https://smspva.com/templates/New_theme/images/flags/64/PY.png) | Paraguay | PY |
| 62 | ![](https://smspva.com/templates/New_theme/images/flags/64/PH.png) | Philippines | PH |
| 63 | ![](https://smspva.com/templates/New_theme/images/flags/64/PL.png) | Poland | PL |
| 64 | ![](https://smspva.com/templates/New_theme/images/flags/64/PT.png) | Portugal | PT |
| 65 | ![](https://smspva.com/templates/New_theme/images/flags/64/RO.png) | Romania | RO |
| 66 | ![](https://smspva.com/templates/New_theme/images/flags/64/RU.png) | Russian Federation | RU |
| 67 | ![](https://smspva.com/templates/New_theme/images/flags/64/RS.png) | Serbia | RS |
| 68 | ![](https://smspva.com/templates/New_theme/images/flags/64/SK.png) | Slovakia | SK |
| 69 | ![](https://smspva.com/templates/New_theme/images/flags/64/SI.png) | Slovenia | SI |
| 70 | ![](https://smspva.com/templates/New_theme/images/flags/64/ZA.png) | South Africa | ZA |
| 71 | ![](https://smspva.com/templates/New_theme/images/flags/64/SE.png) | Sweden | SE |
| 72 | ![](https://smspva.com/templates/New_theme/images/flags/64/TH.png) | Thailand | TH |
| 73 | ![](https://smspva.com/templates/New_theme/images/flags/64/TR.png) | Turkey | TR |
| 74 | ![](https://smspva.com/templates/New_theme/images/flags/64/UA.png) | Ukraine | UA |
| 75 | ![](https://smspva.com/templates/New_theme/images/flags/64/VN.png) | Vietnam | VN |

[](https://docs.smspva.com/#tag/activation_v2_lists/Services-list)Services list
===============================================================================

If you do not find the service you need, then you can use the OTHER (opt19) service or contact support to add the service you need.

| № | Logo | Service | Code |
| --- | --- | --- | --- |
| 1 | ![](https://smspva.com/templates/New_Design/images/ico/open_api.png "service-img") | 1 OpenAI API (chatGPT, DALL-e 2) | opt132 |
| 2 | ![](https://smspva.com/templates/New_Design/images/ico/opt251_66e125780140b.jpg "service-img") | 1cupis.ru | opt251 |
| 3 | ![](https://smspva.com/templates/New_Design/images/ico/opt224_66068262d71e1.png "service-img") | 22bet | opt224 |
| 4 | ![](https://smspva.com/templates/New_Design/images/ico/opt22_655cdab4dbd01.jpg "service-img") | 888casino | opt22 |
| 5 | ![](https://smspva.com/templates/New_Design/images/ico/opt242_668e3f109c6d0.png "service-img") | Abbott | opt242 |
| 6 | ![](https://smspva.com/templates/New_Design/images/ico/nike.png "service-img") | Adidas & Nike | opt86 |
| 7 | ![](https://smspva.com/templates/New_Design/images/ico/airbnb.ico "service-img") | Airbnb | opt46 |
| 8 | ![](https://smspva.com/templates/New_Design/images/ico/taobao.png "service-img") | Alibaba (Taobao, 1688.com) | opt61 |
| 9 | ![](https://smspva.com/templates/New_Design/images/ico/amazon.ico "service-img") | Amazon | opt44 |
| 10 | ![](https://smspva.com/templates/New_Design/images/ico/aol.png "service-img") | AOL | opt10 |
| 11 | ![](https://smspva.com/templates/New_Design/images/ico/apple.ico "service-img") | Apple | opt131 |
| 12 | ![](https://smspva.com/templates/New_Design/images/ico/opt143_655cd99229dba.jpg "service-img") | autocosmos.com | opt143 |
| 13 | ![](https://smspva.com/templates/New_Design/images/ico/avito.png "service-img") | Avito | opt59 |
| 14 | ![](https://smspva.com/templates/New_Design/images/ico/badoo.png "service-img") | Badoo | opt56 |
| 15 | ![](https://smspva.com/templates/New_Design/images/ico/opt209_65801c9cb87c2.png "service-img") | BANDUS | opt209 |
| 16 | ![](https://smspva.com/templates/New_Design/images/ico/opt138_655b124b5ce53.png "service-img") | Bazos.sk | opt138 |
| 17 | ![](https://smspva.com/templates/New_Design/images/ico/opt187_655ca45c48943.png "service-img") | Beget.com | opt187 |
| 18 | ![](https://smspva.com/templates/New_Design/images/ico/opt252_6729d8ff99907.png "service-img") | Best Buy | opt252 |
| 19 | ![](https://smspva.com/templates/New_Design/images/ico/bet365.png "service-img") | bet365 | opt17 |
| 20 | ![](https://smspva.com/templates/New_Design/images/ico/opt192_656ef71f9770d.jpg "service-img") | Betano (+BETANO.ro) | opt192 |
| 21 | ![](https://smspva.com/templates/New_Design/images/ico/betfair.png "service-img") | BetFair | opt25 |
| 22 | ![](https://smspva.com/templates/New_Design/images/ico/opt223_6605370e23fca.jpg "service-img") | Betmgm | opt223 |
| 23 | ![](https://smspva.com/templates/New_Design/images/ico/opt237_66617efa9abc1.png "service-img") | Bitpanda | opt237 |
| 24 | ![](https://smspva.com/templates/New_Design/images/ico/blizzard.ico "service-img") | Blizzard | opt78 |
| 25 | ![](https://smspva.com/templates/New_Design/images/ico/opt135_66630426565d2.png "service-img") | blsspain-russia.com | opt135 |
| 26 | ![](https://smspva.com/templates/New_Design/images/ico/bolt.png "service-img") | Bolt | opt81 |
| 27 | ![](https://smspva.com/templates/New_Design/images/ico/opt217_65c5907f769ab.png "service-img") | Brevo | opt217 |
| 28 | ![](https://smspva.com/templates/New_Design/images/ico/opt145_666304863ecdf.png "service-img") | bumble | opt145 |
| 29 | ![](https://smspva.com/templates/New_Design/images/ico/opt199_6578544374956.png "service-img") | bunq | opt199 |
| 30 | ![](https://smspva.com/templates/New_Design/images/ico/opt137_666304cb5c4b4.png "service-img") | bwin | opt137 |
| 31 | ![](https://smspva.com/templates/New_Design/images/ico/careem.png "service-img") | Careem | opt89 |
| 32 | ![](https://smspva.com/templates/New_Design/images/ico/opt255_6731d0f5bc67e.jpg "service-img") | Casa Pariurilor | opt255 |
| 33 | ![](https://smspva.com/templates/New_Design/images/ico/opt148_6663051dc7573.png "service-img") | casa.it | opt148 |
| 34 | ![](https://smspva.com/templates/New_Design/images/ico/opt226_6618e1e656bbe.png "service-img") | Cash App | opt226 |
| 35 | ![](https://smspva.com/templates/New_Design/images/ico/opt214_658020faa7c45.png "service-img") | Cashrewards | opt214 |
| 36 | ![](https://smspva.com/templates/New_Design/images/ico/opt201_657854eb0dc5e.jpg "service-img") | Casino Plus | opt201 |
| 37 | ![](https://smspva.com/templates/New_Design/images/ico/opt176_655c9e402576d.jpg "service-img") | ChoTot | opt176 |
| 38 | ![](https://smspva.com/templates/New_Design/images/ico/cmobil.ico "service-img") | CityMobil | opt76 |
| 39 | ![](https://smspva.com/templates/New_Design/images/ico/opt196_65703c0312d2f.png "service-img") | Claude (Anthropic) | opt196 |
| 40 | ![](https://smspva.com/templates/New_Design/images/ico/opt98_66630597a465a.png "service-img") | Clubhouse | opt98 |
| 41 | ![](https://smspva.com/templates/New_Design/images/ico/coinbase.png "service-img") | CoinBase | opt112 |
| 42 | ![](https://smspva.com/templates/New_Design/images/ico/contact.ico "service-img") | CONTACT | opt51 |
| 43 | ![](https://smspva.com/templates/New_Design/images/ico/craigslist.ico "service-img") | Craigslist | opt26 |
| 44 | ![](https://smspva.com/templates/New_Design/images/ico/opt124_666305f26e9d5.png "service-img") | Credit Karma | opt124 |
| 45 | ![](https://smspva.com/templates/New_Design/images/ico/opt157_65573a7277542.png "service-img") | CupidMedia | opt157 |
| 46 | ![](https://smspva.com/templates/New_Design/images/ico/opt150_66630661755a6.png "service-img") | Czech email services | opt150 |
| 47 | ![](https://smspva.com/templates/New_Design/images/ico/opt53_666306bc585f2.png "service-img") | Deliveroo | opt53 |
| 48 | ![](https://smspva.com/templates/New_Design/images/ico/opt204_65785f8da5185.png "service-img") | DenimApp | opt204 |
| 49 | ![](https://smspva.com/templates/New_Design/images/ico/didi.ico "service-img") | DiDi | opt92 |
| 50 | ![](https://smspva.com/templates/New_Design/images/ico/discord.ico "service-img") | Discord | opt45 |
| 51 | ![](https://smspva.com/templates/New_Design/images/ico/opt232_66277a123c10d.png "service-img") | DistroKid | opt232 |
| 52 | ![](https://smspva.com/templates/New_Design/images/ico/dodopizza.png "service-img") | Dodopizza + PapaJohns | opt27 |
| 53 | ![](https://smspva.com/templates/New_Design/images/ico/opt40_6663073ae9b40.png "service-img") | Doordash | opt40 |
| 54 | ![](https://smspva.com/templates/New_Design/images/ico/dromru.png "service-img") | Drom.RU | opt32 |
| 55 | ![](https://smspva.com/templates/New_Design/images/ico/drug.png "service-img") | Drug Vokrug | opt31 |
| 56 | ![](https://smspva.com/templates/New_Design/images/ico/opt136_666307d9f04d5.png "service-img") | dundle | opt136 |
| 57 | ![](https://smspva.com/templates/New_Design/images/ico/opt21_6663082ecc1bc.png "service-img") | EasyPay | opt21 |
| 58 | ![](https://smspva.com/templates/New_Design/images/ico/opt200_65785487ae8a7.jpg "service-img") | ENEBA | opt200 |
| 59 | ![](https://smspva.com/templates/New_Design/images/ico/opt248_66becf1d2c4fa.png "service-img") | ESX (abonamentesali.ro) | opt248 |
| 60 | ![](https://smspva.com/templates/New_Design/images/ico/opt141_6663088f13652.png "service-img") | EUROBET | opt141 |
| 61 | ![](https://smspva.com/templates/New_Design/images/ico/fb.png "service-img") | Facebook | opt2 |
| 62 | ![](https://smspva.com/templates/New_Design/images/ico/fastmail.png "service-img") | FastMail | opt43 |
| 63 | ![](https://smspva.com/templates/New_Design/images/ico/opt215_658023186e69f.png "service-img") | Fbet | opt215 |
| 64 | ![](https://smspva.com/templates/New_Design/images/ico/opt159_65573af945053.png "service-img") | Feeld | opt159 |
| 65 | ![](https://smspva.com/templates/New_Design/images/ico/opt6_666308f6e6723.png "service-img") | Fiverr | opt6 |
| 66 | ![](https://smspva.com/templates/New_Design/images/ico/opt139_666309490c426.png "service-img") | fontbet | opt139 |
| 67 | ![](https://smspva.com/templates/New_Design/images/ico/opt189_655ca5f13c9b3.png "service-img") | foodora | opt189 |
| 68 | ![](https://smspva.com/templates/New_Design/images/ico/foodpanda.png "service-img") | foodpanda | opt115 |
| 69 | ![](https://smspva.com/templates/New_Design/images/ico/opt221_65f2a3c9c749c.png "service-img") | Fortuna | opt221 |
| 70 | ![](https://smspva.com/templates/New_Design/images/ico/fotostrana.png "service-img") | Fotostrana | opt13 |
| 71 | ![](https://smspva.com/templates/New_Design/images/ico/opt142_6663098613401.png "service-img") | funpay | opt142 |
| 72 | ![](https://smspva.com/templates/New_Design/images/ico/g2a.jpg "service-img") | G2A.COM | opt68 |
| 73 | ![](https://smspva.com/templates/New_Design/images/ico/paxful.png "service-img") | Gameflip | opt77 |
| 74 | ![](https://smspva.com/templates/New_Design/images/ico/opt28_666309e76d144.png "service-img") | Gamers set (offgamers.com, G2A.com, seagm.com) | opt28 |
| 75 | ![](https://smspva.com/templates/New_Design/images/ico/opt179_655ca016d7361.png "service-img") | GetsBet.ro | opt179 |
| 76 | ![](https://smspva.com/templates/New_Design/images/ico/gettaxi.png "service-img") | GetTaxi | opt35 |
| 77 | ![](https://smspva.com/templates/New_Design/images/ico/opt188_655ca591689ef.png "service-img") | GGbet | opt188 |
| 78 | ![](https://smspva.com/templates/New_Design/images/ico/opt229_6627781a653e5.jpg "service-img") | GGPokerUK | opt229 |
| 79 | ![](https://smspva.com/templates/New_Design/images/ico/opt85_66630a3f4b444.png "service-img") | giocodigitale.it | opt85 |
| 80 | ![](https://smspva.com/templates/New_Design/images/ico/glovoraketa.ico "service-img") | Glovo & Raketa | opt108 |
| 81 | ![](https://smspva.com/templates/New_Design/images/ico/opt240_66879c1ad054d.jpg "service-img") | goldbet.it | opt240 |
| 82 | ![](https://smspva.com/templates/New_Design/images/ico/gmail.png "service-img") | Google (YouTube, Gmail) | opt1 |
| 83 | ![](https://smspva.com/templates/New_Design/images/ico/gmail.png "service-img") | Google Voice | opt140 |
| 84 | ![](https://smspva.com/templates/New_Design/images/ico/grabtaxi.png "service-img") | GrabTaxi | opt30 |
| 85 | ![](https://smspva.com/templates/New_Design/images/ico/grailed.png "service-img") | Grailed | opt420 |
| 86 | ![](https://smspva.com/templates/New_Design/images/ico/grindr.ico "service-img") | Grindr | opt110 |
| 87 | ![](https://smspva.com/templates/New_Design/images/ico/opt155_655716304f898.png "service-img") | Happn | opt155 |
| 88 | ![](https://smspva.com/templates/New_Design/images/ico/opt203_65785efc1689c.png "service-img") | HelloTalk | opt203 |
| 89 | ![](https://smspva.com/templates/New_Design/images/ico/opt238_667a2c8e7a580.png "service-img") | hepsiburada | opt238 |
| 90 | ![](https://smspva.com/templates/New_Design/images/ico/opt216_65a5f5900f846.png "service-img") | Hey | opt216 |
| 91 | ![](https://smspva.com/templates/New_Design/images/ico/opt120_66630aaf1328d.png "service-img") | Hinge | opt120 |
| 92 | ![](https://smspva.com/templates/New_Design/images/ico/opt144_66630aea202ae.png "service-img") | hopper | opt144 |
| 93 | ![](https://smspva.com/templates/New_Design/images/ico/opt166_6556153845310.png "service-img") | HUAWEI | opt166 |
| 94 | ![](https://smspva.com/templates/New_Design/images/ico/icard.png "service-img") | ICard | opt103 |
| 95 | ![](https://smspva.com/templates/New_Design/images/ico/opt165_66630b4899f30.png "service-img") | idealista.com | opt165 |
| 96 | ![](https://smspva.com/templates/New_Design/images/ico/opt55_66630b89aff92.png "service-img") | ifood | opt55 |
| 97 | ![](https://smspva.com/templates/New_Design/images/ico/imo.png "service-img") | IMO | opt111 |
| 98 | ![](https://smspva.com/templates/New_Design/images/ico/opt167_654de72ab4120.png "service-img") | inbox.lv | opt167 |
| 99 | ![](https://smspva.com/templates/New_Design/images/ico/inboxdollars.png "service-img") | Inboxdollars | opt118 |
| 100 | ![](https://smspva.com/templates/New_Design/images/ico/instagram.png "service-img") | Instagram (+Threads) | opt16 |
| 101 | ![](https://smspva.com/templates/New_Design/images/ico/opt193_65702a87b9141.png "service-img") | Ipsos | opt193 |
| 102 | ![](https://smspva.com/templates/New_Design/images/ico/opt243_6694df3aa6431.png "service-img") | IQOS | opt243 |
| 103 | ![](https://smspva.com/templates/New_Design/images/ico/jd.ico "service-img") | JD.com | opt94 |
| 104 | ![](https://smspva.com/templates/New_Design/images/ico/kakao.ico "service-img") | KakaoTalk | opt71 |
| 105 | ![](https://smspva.com/templates/New_Design/images/ico/opt175_655c995f936a3.png "service-img") | Klarna | opt175 |
| 106 | ![](https://smspva.com/templates/New_Design/images/ico/opt152_66630bd9c5aae.png "service-img") | kleinanzeigen.de | opt152 |
| 107 | ![](https://smspva.com/templates/New_Design/images/ico/opt99_66630c05209e0.png "service-img") | KoronaPay | opt99 |
| 108 | ![](https://smspva.com/templates/New_Design/images/ico/sbermarket.ico "service-img") | Kuper (SberMarket) | opt97 |
| 109 | ![](https://smspva.com/templates/New_Design/images/ico/kwiff.ico "service-img") | kwiff.com | opt129 |
| 110 | ![](https://smspva.com/templates/New_Design/images/ico/opt195_6570395fe0b3f.png "service-img") | Lajumate.ro | opt195 |
| 111 | ![](https://smspva.com/templates/New_Design/images/ico/opt180_655ca0b0de4b5.png "service-img") | Lalamove | opt180 |
| 112 | ![](https://smspva.com/templates/New_Design/images/ico/opt182_655ca1d5514bf.png "service-img") | LAPOSTE | opt182 |
| 113 | ![](https://smspva.com/templates/New_Design/images/ico/opt222_65f2a3fbe362f.jpg "service-img") | LASVEGAS.RO | opt222 |
| 114 | ![](https://smspva.com/templates/New_Design/images/ico/lazada.png "service-img") | Lazada | opt60 |
| 115 | ![](https://smspva.com/templates/New_Design/images/ico/opt164_65571a978d6e3.png "service-img") | Leboncoin | opt164 |
| 116 | ![](https://smspva.com/templates/New_Design/images/ico/line.ico "service-img") | Line Messenger | opt37 |
| 117 | ![](https://smspva.com/templates/New_Design/images/ico/linkedin.png "service-img") | LinkedIn | opt8 |
| 118 | ![](https://smspva.com/templates/New_Design/images/ico/opt245_66a453a3a5454.png "service-img") | Linode | opt245 |
| 119 | ![](https://smspva.com/templates/New_Design/images/ico/livescore.png "service-img") | LiveScore | opt42 |
| 120 | ![](https://smspva.com/templates/New_Design/images/ico/localbitcoins.png "service-img") | LocalBitcoins | opt105 |
| 121 | ![](https://smspva.com/templates/New_Design/images/ico/locanto.jpg "service-img") | Locanto.com | opt114 |
| 122 | ![](https://smspva.com/templates/New_Design/images/ico/lyft.ico "service-img") | Lyft | opt75 |
| 123 | ![](https://smspva.com/templates/New_Design/images/ico/opt126_66630c9094b53.png "service-img") | Magnit | opt126 |
| 124 | ![](https://smspva.com/templates/New_Design/images/ico/mail_black.png "service-img") | Mail.RU | opt33 |
| 125 | ![](https://smspva.com/templates/New_Design/images/ico/mailru.png "service-img") | Mail.ru Group | opt4 |
| 126 | ![](https://smspva.com/templates/New_Design/images/ico/mamba.ico "service-img") | Mamba | opt100 |
| 127 | ![](https://smspva.com/templates/New_Design/images/ico/opt171_6556077d514ef.jpg "service-img") | Marktplaats | opt171 |
| 128 | ![](https://smspva.com/templates/New_Design/images/ico/opt250_66e00cff34986.png "service-img") | Match | opt250 |
| 129 | ![](https://smspva.com/templates/New_Design/images/ico/opt219_65d85aacb2f0a.png "service-img") | maxline.by | opt219 |
| 130 | ![](https://smspva.com/templates/New_Design/images/ico/michat.png "service-img") | MiChat | opt96 |
| 131 | ![](https://smspva.com/templates/New_Design/images/ico/ms.png "service-img") | Microsoft (Azure, Bing, Skype, etc) | opt15 |
| 132 | ![](https://smspva.com/templates/New_Design/images/ico/opt156_655739cc1a3db.png "service-img") | mobileDE | opt156 |
| 133 | ![](https://smspva.com/templates/New_Design/images/ico/opt184_655ca302f1b2a.png "service-img") | MOMO | opt184 |
| 134 | ![](https://smspva.com/templates/New_Design/images/ico/monese.png "service-img") | Monese | opt121 |
| 135 | ![](https://smspva.com/templates/New_Design/images/ico/opt47_66630ce033c02.png "service-img") | MoneyLion | opt47 |
| 136 | ![](https://smspva.com/templates/New_Design/images/ico/opt254_67316d1b182a8.png "service-img") | Monster Energy | opt254 |
| 137 | ![](https://smspva.com/templates/New_Design/images/ico/opt197_65785390376e5.png "service-img") | MPSellers | opt197 |
| 138 | ![](https://smspva.com/templates/New_Design/images/ico/opt211_65801f33ea021.png "service-img") | MrGreen | opt211 |
| 139 | ![](https://smspva.com/templates/New_Design/images/ico/office365.ico "service-img") | MS Office 365 | opt7 |
| 140 | ![](https://smspva.com/templates/New_Design/images/ico/opt0_66630d21d0979.png "service-img") | myopinions & erewards | opt0 |
| 141 | ![](https://smspva.com/templates/New_Design/images/ico/naver.ico "service-img") | Naver | opt73 |
| 142 | ![](https://smspva.com/templates/New_Design/images/ico/opt198_657853fe74459.png "service-img") | Nectar | opt198 |
| 143 | ![](https://smspva.com/templates/New_Design/images/ico/netbet.ico "service-img") | NetBet | opt95 |
| 144 | ![](https://smspva.com/templates/New_Design/images/ico/neteller.ico "service-img") | Neteller | opt116 |
| 145 | ![](https://smspva.com/templates/New_Design/images/ico/netflix.ico "service-img") | Netflix | opt101 |
| 146 | ![](https://smspva.com/templates/New_Design/images/ico/opt202_65785e5c99854.jpg "service-img") | NHNCloud | opt202 |
| 147 | ![](https://smspva.com/templates/New_Design/images/ico/opt177_655c9ed951f22.png "service-img") | NHNcorp (강남언니) | opt177 |
| 148 | ![](https://smspva.com/templates/New_Design/images/ico/opt119_66630d716253d.png "service-img") | Nico | opt119 |
| 149 | ![](https://smspva.com/templates/New_Design/images/ico/opt151_66630d9ecbf7a.png "service-img") | novibet.com | opt151 |
| 150 | ![](https://smspva.com/templates/New_Design/images/ico/ok.png "service-img") | OD | opt5 |
| 151 | ![](https://smspva.com/templates/New_Design/images/ico/offerup.png "service-img") | OfferUp | opt113 |
| 152 | ![](https://smspva.com/templates/New_Design/images/ico/opt230_6627790906252.png "service-img") | OkCupid | opt230 |
| 153 | ![](https://smspva.com/templates/New_Design/images/ico/opt228_662776c65aa6f.png "service-img") | OKX | opt228 |
| 154 | ![](https://smspva.com/templates/New_Design/images/ico/olx.png "service-img") | OLX + goods.ru | opt70 |
| 155 | ![](https://smspva.com/templates/New_Design/images/ico/opt241_668b5cc59eed1.png "service-img") | onet.pl (Onet Konto) | opt241 |
| 156 | ![](https://smspva.com/templates/New_Design/images/ico/another.png "service-img") | OTHER (no guarantee) | opt19 |
| 157 | ![](https://smspva.com/templates/New_Design/images/ico/another.png "service-img") | OTHER (voice code) | opt00019 |
| 158 | ![](https://smspva.com/templates/New_Design/images/ico/opt212_65801fe22156e.png "service-img") | OurTime | opt212 |
| 159 | ![](https://smspva.com/templates/New_Design/images/ico/opt246_66a75c27314ca.jpg "service-img") | Outlier | opt246 |
| 160 | ![](https://smspva.com/templates/New_Design/images/ico/opt181_655ca17d51618.jpg "service-img") | OZON.ru | opt181 |
| 161 | ![](https://smspva.com/templates/New_Design/images/ico/paddypower.png "service-img") | Paddy Power | opt109 |
| 162 | ![](https://smspva.com/templates/New_Design/images/ico/opt169_65573ba54b8e3.png "service-img") | Pari.ru | opt169 |
| 163 | ![](https://smspva.com/templates/New_Design/images/ico/opt3_66630e40af702.png "service-img") | Parimatch | opt3 |
| 164 | ![](https://smspva.com/templates/New_Design/images/ico/opt162_655739fca1cbc.png "service-img") | Payoneer | opt162 |
| 165 | ![](https://smspva.com/templates/New_Design/images/ico/paypal.ico "service-img") | PayPal + Ebay | opt83 |
| 166 | ![](https://smspva.com/templates/New_Design/images/ico/opt122_66630e6507056.png "service-img") | Paysafecard | opt122 |
| 167 | ![](https://smspva.com/templates/New_Design/images/ico/opt183_655ca25582e36.png "service-img") | PAYSEND | opt183 |
| 168 | ![](https://smspva.com/templates/New_Design/images/ico/opt149_666315091b834.png "service-img") | pm.by | opt149 |
| 169 | ![](https://smspva.com/templates/New_Design/images/ico/pof.ico "service-img") | POF.com | opt84 |
| 170 | ![](https://smspva.com/templates/New_Design/images/ico/promua.ico "service-img") | Prom.UA | opt107 |
| 171 | ![](https://smspva.com/templates/New_Design/images/ico/protonmail.ico "service-img") | Proton Mail | opt57 |
| 172 | ![](https://smspva.com/templates/New_Design/images/ico/opt207_657860f02ca12.png "service-img") | Publi24 | opt207 |
| 173 | ![](https://smspva.com/templates/New_Design/images/ico/qiwi.png "service-img") | Qiwi | opt18 |
| 174 | ![](https://smspva.com/templates/New_Design/images/ico/opt247_66aaf3ff6e25b.png "service-img") | RadQuest | opt247 |
| 175 | ![](https://smspva.com/templates/New_Design/images/ico/opt154_65573c1d9ffef.png "service-img") | Rambler.ru | opt154 |
| 176 | ![](https://smspva.com/templates/New_Design/images/ico/opt133_6663154f63220.png "service-img") | Revolut | opt133 |
| 177 | ![](https://smspva.com/templates/New_Design/images/ico/opt153_65573b772b37d.png "service-img") | ROOMSTER | opt153 |
| 178 | ![](https://smspva.com/templates/New_Design/images/ico/opt170_65573bf46bb42.png "service-img") | Royal Canin | opt170 |
| 179 | ![](https://smspva.com/templates/New_Design/images/ico/opt186_655ca4149ac53.png "service-img") | RusDate | opt186 |
| 180 | ![](https://smspva.com/templates/New_Design/images/ico/opt185_655ca34cacf3f.png "service-img") | Samokat | opt185 |
| 181 | ![](https://smspva.com/templates/New_Design/images/ico/opt174_655c93471955e.png "service-img") | Samsung | opt174 |
| 182 | ![](https://smspva.com/templates/New_Design/images/ico/opt134_66631584e443d.png "service-img") | Schibsted-konto | opt134 |
| 183 | ![](https://smspva.com/templates/New_Design/images/ico/shopee.ico "service-img") | Shopee | opt48 |
| 184 | ![](https://smspva.com/templates/New_Design/images/ico/signal.png "service-img") | Signal | opt127 |
| 185 | ![](https://smspva.com/templates/New_Design/images/ico/opt38_666315d27fd60.png "service-img") | Sisal | opt38 |
| 186 | ![](https://smspva.com/templates/New_Design/images/ico/skout.png "service-img") | Skout | opt49 |
| 187 | ![](https://smspva.com/templates/New_Design/images/ico/skrill.ico "service-img") | Skrill | opt117 |
| 188 | ![](https://smspva.com/templates/New_Design/images/ico/snapchat.ico "service-img") | Snapchat | opt90 |
| 189 | ![](https://smspva.com/templates/New_Design/images/ico/opt190_66631618b8f0f.png "service-img") | SNKRDUNK | opt190 |
| 190 | ![](https://smspva.com/templates/New_Design/images/ico/opt234_66277c31c97c6.jpg "service-img") | Solitaire Cash | opt234 |
| 191 | ![](https://smspva.com/templates/New_Design/images/ico/steam.png "service-img") | Steam | opt58 |
| 192 | ![](https://smspva.com/templates/New_Design/images/ico/opt146_6663166e99628.png "service-img") | subito.it | opt146 |
| 193 | ![](https://smspva.com/templates/New_Design/images/ico/opt249_66cd532e50a46.jpg "service-img") | Superbet | opt249 |
| 194 | ![](https://smspva.com/templates/New_Design/images/ico/swagbucks.ico "service-img") | Swagbucks | opt125 |
| 195 | ![](https://smspva.com/templates/New_Design/images/ico/tango.jpg "service-img") | Tango | opt82 |
| 196 | ![](https://smspva.com/templates/New_Design/images/ico/opt161_65573bd0db8b8.jpg "service-img") | TANK.RU | opt161 |
| 197 | ![](https://smspva.com/templates/New_Design/images/ico/opt239_6686a402c737d.jpg "service-img") | Taptap | opt239 |
| 198 | ![](https://smspva.com/templates/New_Design/images/ico/taxi_maxim.png "service-img") | Taxi Maksim | opt74 |
| 199 | ![](https://smspva.com/templates/New_Design/images/ico/telegram.png "service-img") | Telegram | opt29 |
| 200 | ![](https://smspva.com/templates/New_Design/images/ico/telegram.png "service-img") | Telegram (voice code) | opt00029 |
| 201 | ![](https://smspva.com/templates/New_Design/images/ico/qq.png "service-img") | Tencent QQ | opt34 |
| 202 | ![](https://smspva.com/templates/New_Design/images/ico/ticketmaster.ico "service-img") | Ticketmaster | opt52 |
| 203 | ![](https://smspva.com/templates/New_Design/images/ico/tiktok.png "service-img") | TikTok | opt104 |
| 204 | ![](https://smspva.com/templates/New_Design/images/ico/tinder.png "service-img") | Tinder | opt9 |
| 205 | ![](https://smspva.com/templates/New_Design/images/ico/opt235_66277cfea7c12.png "service-img") | TLScontact | opt235 |
| 206 | ![](https://smspva.com/templates/New_Design/images/ico/opt191_656ef49a40563.jpg "service-img") | TopCashback | opt191 |
| 207 | ![](https://smspva.com/templates/New_Design/images/ico/opt220_65f2a39a0ebef.jpg "service-img") | TOTOGAMING | opt220 |
| 208 | ![](https://smspva.com/templates/New_Design/images/ico/opt218_65cdde639ba36.png "service-img") | TransferGo | opt218 |
| 209 | ![](https://smspva.com/templates/New_Design/images/ico/opt233_66277b08f3960.png "service-img") | TrueCaller | opt233 |
| 210 | ![](https://smspva.com/templates/New_Design/images/ico/opt244_6697a1805c2c2.png "service-img") | Truth Social | opt244 |
| 211 | ![](https://smspva.com/templates/New_Design/images/ico/twilio.png "service-img") | Twilio | opt66 |
| 212 | ![](https://smspva.com/templates/New_Design/images/ico/opt205_657860147869a.png "service-img") | Twitch | opt205 |
| 213 | ![](https://smspva.com/templates/New_Design/images/ico/opt160_65573ac5a1791.png "service-img") | U By Prodia | opt160 |
| 214 | ![](https://smspva.com/templates/New_Design/images/ico/uber.jpg "service-img") | Uber | opt72 |
| 215 | ![](https://smspva.com/templates/New_Design/images/ico/opt39_666316ca23ffd.png "service-img") | Verse | opt39 |
| 216 | ![](https://smspva.com/templates/New_Design/images/ico/viber.png "service-img") | Viber | opt11 |
| 217 | ![](https://smspva.com/templates/New_Design/images/ico/vinted.png "service-img") | Vinted | opt130 |
| 218 | ![](https://smspva.com/templates/New_Design/images/ico/vk_black.png "service-img") | VK (no guarantee) | opt69 |
| 219 | ![](https://smspva.com/templates/New_Design/images/ico/opt178_655c9fa709a13.png "service-img") | VonageVF | opt178 |
| 220 | ![](https://smspva.com/templates/New_Design/images/ico/opt147_6663171214afb.png "service-img") | VooV Meeting | opt147 |
| 221 | ![](https://smspva.com/templates/New_Design/images/ico/opt213_6580204be0c7e.jpg "service-img") | Waitomo | opt213 |
| 222 | ![](https://smspva.com/templates/New_Design/images/ico/opt206_65786091bfe43.png "service-img") | WalletHub | opt206 |
| 223 | ![](https://smspva.com/templates/New_Design/images/ico/opt227_66275f39aa809.png "service-img") | Walmart | opt227 |
| 224 | ![](https://smspva.com/templates/New_Design/images/ico/opt172_655c87eca1f10.png "service-img") | WEB.DE | opt172 |
| 225 | ![](https://smspva.com/templates/New_Design/images/ico/webmoney.png "service-img") | WebMoney&ENUM | opt24 |
| 226 | ![](https://smspva.com/templates/New_Design/images/ico/wechat.png "service-img") | WeChat | opt67 |
| 227 | ![](https://smspva.com/templates/New_Design/images/ico/weebly.png "service-img") | Weebly | opt54 |
| 228 | ![](https://smspva.com/templates/New_Design/images/ico/weststein.ico "service-img") | WESTSTEIN | opt80 |
| 229 | ![](https://smspva.com/templates/New_Design/images/ico/opt231_6627797fc0648.png "service-img") | Whatnot | opt231 |
| 230 | ![](https://smspva.com/templates/New_Design/images/ico/whatsapp.png "service-img") | WhatsAPP | opt20 |
| 231 | ![](https://smspva.com/templates/New_Design/images/ico/whatsapp.png "service-img") | WhatsAPP (voice code) | opt00020 |
| 232 | ![](https://smspva.com/templates/New_Design/images/ico/whoosh.ico "service-img") | Whoosh | opt123 |
| 233 | ![](https://smspva.com/templates/New_Design/images/ico/opt106_66631774989da.png "service-img") | Wing Money | opt106 |
| 234 | ![](https://smspva.com/templates/New_Design/images/ico/opt91_666317b2b934e.png "service-img") | Wise | opt91 |
| 235 | ![](https://smspva.com/templates/New_Design/images/ico/opt163_655607e9a3566.jpg "service-img") | Wolt | opt163 |
| 236 | ![](https://smspva.com/templates/New_Design/images/ico/opt208_6578614116272.png "service-img") | WooPlus | opt208 |
| 237 | ![](https://smspva.com/templates/New_Design/images/ico/twitter.png "service-img") | X (Twitter) | opt41 |
| 238 | ![](https://smspva.com/templates/New_Design/images/ico/opt173_655c907dc253f.png "service-img") | X World Wallet | opt173 |
| 239 | ![](https://smspva.com/templates/New_Design/images/ico/yahoo.png "service-img") | Yahoo | opt65 |
| 240 | ![](https://smspva.com/templates/New_Design/images/ico/yalla.png "service-img") | Yalla.live | opt88 |
| 241 | ![](https://smspva.com/templates/New_Design/images/ico/yandex.png "service-img") | Yandex&YooMoney | opt23 |
| 242 | ![](https://smspva.com/templates/New_Design/images/ico/opt236_66545076f0f9e.png "service-img") | Year13 | opt236 |
| 243 | ![](https://smspva.com/templates/New_Design/images/ico/opt158_65560834b69e9.png "service-img") | Zalo | opt158 |
| 244 | ![](https://smspva.com/templates/New_Design/images/ico/opt225_66068297c8f5e.png "service-img") | Zasilkovna | opt225 |
| 245 | ![](https://smspva.com/templates/New_Design/images/ico/zoho.png "service-img") | Zoho | opt93 |
| 246 | ![](https://smspva.com/templates/New_Design/images/ico/opt194_657030a853861.png "service-img") | ZoomInfo | opt194 |
| 247 | ![](https://smspva.com/templates/New_Design/images/ico/opt253_672c28e72b044.png "service-img") | Zoosk | opt253 |

[](https://docs.smspva.com/#tag/activation_all_methods)All requests
===================================================================

[](https://docs.smspva.com/#tag/activation_all_methods/operation/getUserByName)Getting phone number
---------------------------------------------------------------------------------------------------

Request for receiving a phone number for a certain service

##### Authorizations:

*apikey*

##### query Parameters

| apikey

required

 |

string

Example: apikey=DSWAFvdedrE4

Your API key

 |
| service

required

 |

string

Example: service=opt4

Service code

 |
| country

required

 |

string

Example: country=RU

Country code

 |
| metod

required

 |

string

Example: metod=get_number

Method name

 |

### Responses

**200**

Success

##### Response Schema: application/json

| response |

string

Example: "2"

Status

 |
| number |

string

Example: "9871234567"

Number to receive SMS

 |
| id |

string

Example: "25623"

Order ID

 |

get/priemnik.php?method=get_number

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/priemnik.php?apikey=DSWAFvdedrE4&service=opt4&country=RU&metod=get_number&method=get_number'\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Copy

`{

-   "response": "2",

-   "number": "9871234567",

-   "id": "25623"

}`

[](https://docs.smspva.com/#tag/activation_all_methods/operation/get_sms)Getting SMS
------------------------------------------------------------------------------------

Receiving an SMS for a certain service\
In this method id parameter is indicated from the response to request for phone number get_number

> **Note**\
>\
> If you get the response that a code from SMS hasn't been found yet, send request get_sms once again 20 seconds later. Note, the server searches for SMS for 10 minutes. You need to send your request within 10 minutes each 20 seconds per one request. That said, you receive a code from SMS or error message.\
**Code Refinement**\
If you want to get re-SMS without closing the order (Code Refinement), then just on the method get_sms add additional parameter sms=sms Example string:

 https://smspva.com/priemnik.php?\
 metod=get_sms\
 &country=ru\
 &service=opt4\
 &id=25623\
 &apikey=DSWAFvdedrE4\
 &sms=sms\
In this case, your order can not be closed and you may receive a re-SMS. Re-chargeable SMS. The cost is the cost of an ordinary SMS for this service.

##### Authorizations:

*apikey*

##### query Parameters

| apikey

required

 |

string

Example: apikey=DSWAFvdedrE4

Your API key

 |
| service

required

 |

string

Example: service=opt4

Service code

 |
| country

required

 |

string

Example: country=RU

Country code

 |
| id

required

 |

string

Example: id=3421

ID of the order

 |
| metod

required

 |

string

Example: metod=get_sms

Method name

 |

### Responses

**200**

Success

##### Response Schema: application/json

| response |

string

Example: "2"

Status

 |
| number |

string

Example: "9871234567"

Number to receive SMS

 |
| sms |

string

Example: "234562"

Code from SMS

 |

get/priemnik.php?method=get_sms

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/priemnik.php?apikey=DSWAFvdedrE4&service=opt4&country=RU&id=3421&metod=get_sms&method=get_sms'\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Copy

`{

-   "response": 2,

-   "number": "9871234567",

-   "sms": "234562"

}`

[](https://docs.smspva.com/#tag/activation_all_methods/operation/get_balance)Cancelling order
---------------------------------------------------------------------------------------------

Get the user's balance information.

##### Authorizations:

*apikey*

##### query Parameters

| apikey

required

 |

string

Example: apikey=DSWAFvdedrE4

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |

### Responses

**200**

Success

##### Response Schema: application/json

| response |

string

Example: "1"

Status

 |
| balance |

string

Example: "385.00"

Current balance

 |

get/priemnik.php?method=get_balance

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/priemnik.php?apikey=DSWAFvdedrE4&method=get_balance'\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Copy

`{

-   "response": "1",

-   "balance": "385.00"

}`

[](https://docs.smspva.com/#tag/activation_all_methods/operation/get_userinfo)Getting information about user balance
--------------------------------------------------------------------------------------------------------------------

Get the user's balance and karma information.

##### Authorizations:

*apikey*

##### query Parameters

| apikey

required

 |

string

Example: apikey=DSWAFvdedrE4

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| service

required

 |

string

Example: service=opt4

Services code (see services list)

 |
| metod

required

 |

string

Example: metod=get_userinfo

Method name

 |

### Responses

**200**

Success

##### Response Schema: application/json

| response |

integer

Example: "1"

Status

 |
| balance |

string

Example: "385.00"

Current balance

 |
| karma |

string

Example: "10"

Current rating value

 |

get/priemnik.php?method=get_userinfo

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/priemnik.php?apikey=DSWAFvdedrE4&service=opt4&metod=get_userinfo&method=get_userinfo'\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Copy

`{

-   "response": 1,

-   "balance": "385.00",

-   "karma": "10"

}`

[](https://docs.smspva.com/#tag/activation_all_methods/operation/denial)Cancelling order
----------------------------------------------------------------------------------------

Cancel the order to the number you received

##### Authorizations:

*apikey*

##### query Parameters

| apikey

required

 |

string

Example: apikey=DSWAFvdedrE4

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| service |

string

Example: service=opt4

Services code (see services list)

 |
| country |

string

Example: country=RU

Countries code (countries list)

 |
| id

required

 |

string

Example: id=3212

Order id

 |
| metod

required

 |

string

Example: metod=denial

Method name

 |

### Responses

**200**

Success

##### Response Schema: application/json

| response |

string

Example: "2"

Status

 |
| number |

string

Example: ""

Phone number

 |
| id |

string

Example: ""

Order id

 |

get/priemnik.php?method=denial

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/priemnik.php?apikey=DSWAFvdedrE4&service=opt4&country=RU&id=3212&metod=denial&method=denial'\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Copy

`{

-   "response": "2",

-   "number": "",

-   "id": ""

}`

[](https://docs.smspva.com/#tag/activation_all_methods/operation/ban)Banning phone number
-----------------------------------------------------------------------------------------

Report to the server that the number is already used

##### Authorizations:

*apikey*

##### query Parameters

| apikey

required

 |

string

Example: apikey=DSWAFvdedrE4

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| service

required

 |

string

Example: service=opt4

Services code (see services list)

 |
| id

required

 |

integer

Example: id=3212

Order id

 |
| metod

required

 |

string

Example: metod=ban

Method name

 |

### Responses

**200**

Success

##### Response Schema: application/json

| response |

string

Example: "2"

Status

 |
| number |

string

Example: ""

Phone number

 |
| id |

string

Example: ""

Order id

 |

get/priemnik.php?method=ban

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/priemnik.php?apikey=DSWAFvdedrE4&service=opt4&id=3212&metod=ban&method=ban'\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Copy

`{

-   "response": 2,

-   "number": "",

-   "id": ""

}`

[](https://docs.smspva.com/#tag/activation_all_methods/operation/get_clearsms)Removing old SMS for receiving new SMS
--------------------------------------------------------------------------------------------------------------------

Checking phone number for receiving few sms ID is order identificator.

> **Note** > > After checking phone number using get_clearsms, need to make get_sms request

##### Authorizations:

*apikey*

##### query Parameters

| apikey

required

 |

string

Example: apikey=DSWAFvdedrE4

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| service

required

 |

string

Example: service=opt4

Services code (see services list)

 |
| id

required

 |

string

Order id

 |
| metod

required

 |

string

Example: metod=get_clearsms

Method name

 |

### Responses

**200**

Success

##### Response Schema: application/json

| response |

string

Example: "2"

Status

 |
| clearsms |

string

Example: "ok"

Result of operation

 |

get/priemnik.php?method=get_clearsms

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/priemnik.php?apikey=DSWAFvdedrE4&service=opt4&id=SOME_STRING_VALUE&metod=get_clearsms&method=get_clearsms'\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Copy

`{

-   "response": "2",

-   "clearsms": "ok"

}`

[](https://docs.smspva.com/#tag/activation_all_methods/operation/get_count_new)Getting count of available phones
----------------------------------------------------------------------------------------------------------------

Request for the amount of free activations for a certain service

##### Authorizations:

*apikey*

##### query Parameters

| apikey

required

 |

string

Example: apikey=DSWAFvdedrE4

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| service

required

 |

string

Example: service=opt4

Services code (see services list)

 |
| country

required

 |

string

Example: country=RU

Countries code (countries list)

 |

### Responses

**200**

Success

##### Response Schema: application/json

| service |

string

Example: "opt5"

Services code (see services list)

 |
| online |

integer

Example: "128"

Number of available now

 |
| total |

integer

Example: "228"

Total available

 |
| forTotal |

integer

Example: "10"

Available now for call forwarding

 |
| forOnline |

integer

Example: "20"

Total available for call forwarding

 |
| country |

string

Example: "RU"

Country code

 |

get/priemnik.php?method=get_count_new

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/priemnik.php?apikey=DSWAFvdedrE4&service=opt4&country=RU&method=get_count_new'\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Copy

`{

-   "service": "opt5",

-   "online": 128,

-   "total": 228,

-   "forTotal": 10,

-   "forOnline": 20,

-   "country": "RU"

}`

[](https://docs.smspva.com/#tag/activation_all_methods/operation/get_service_price)Getting prices for SMS
---------------------------------------------------------------------------------------------------------

Request the current price for SMS for a country and service

##### Authorizations:

*apikey*

##### query Parameters

| apikey

required

 |

string

Example: apikey=DSWAFvdedrE4

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| service

required

 |

string

Example: service=opt4

Services code (see services list)

 |
| country

required

 |

string

Example: country=RU

Countries code (countries list)

 |

### Responses

**200**

Success

##### Response Schema: application/json

| response |

string

Example: "1"

Status

 |
| country |

string

Example: "EN"

Countries code (countries list)

 |
| service |

string

Example: "opt4"

Services code (see services list)

 |
| price |

string

Example: "0.50"

The price of receiving 1 SMS

 |

get/priemnik.php?method=get_service_price

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/priemnik.php?apikey=DSWAFvdedrE4&service=opt4&country=RU&method=get_service_price'\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Copy

`{

-   "response": 1,

-   "country": "EN",

-   "service": "opt4",

-   "price": "0.50"

}`

[](https://docs.smspva.com/#tag/activation_all_methods/operation/get_proverka)Checking availability for receiving SMS
---------------------------------------------------------------------------------------------------------------------

Checking the numbers for multiple SMS In this method, number parameter specifies the number that you want to check.

> **Note**
>
> Following the successful check of a number, send a request for getting the number - get_number ALSO with number parameter. To check SMS send a request for SMS get_sms according to conditions

##### Authorizations:

*apikey*

##### query Parameters

| apikey

required

 |

string

Your API key\
You can find it on the website in the top right drop-down menu in the Profile and APIKEY section

 |
| number

required

 |

string

Phone number

 |
| service

required

 |

string

Services code (see services list)

 |

### Responses

**200**

Success

##### Response Schema: application/json

One of 

SuccessError. Phone numbers is incorrectError. Previous order not foundError. Previous order not foundError. Modem is busyError. Modem is busy

| response |

string

Example: "ok"

Status

 |
| number |

string

Example: "9685156912"

Number to receive SMS

 |
| id |

integer

Example: "25623"

Order ID

 |

get/priemnik.php?method=get_proverka

### Request samples

-   Shell + Curl
-   Php + Curl
-   Node + Request
-   Python + Python3

Copy

curl --request GET\
  --url 'https://smspva.com/priemnik.php?apikey=SOME_STRING_VALUE&number=SOME_STRING_VALUE&service=SOME_STRING_VALUE&method=get_proverka'\
  --header 'apikey: REPLACE_KEY_VALUE'

### Response samples

-   200

Content type

application/json

Example

SuccessError. Phone numbers is incorrectError. Previous order not foundError. Modem is busySuccess

Copy

`{

-   "response": "ok",

-   "number": "9685156912",

-   "id": 25623

}`

[](https://docs.smspva.com/#tag/activation_errors)General provisions and list of errors
=======================================================================================

[](https://docs.smspva.com/#tag/activation_errors/Errors-list)Errors list
=========================================================================

| Response code | Meaning |
| --- | --- |
| 5 | You have exceeded the number of requests per minute. |
| 6 | You will be banned for 10 minutes, because scored negative karma. |
| 7 | You have exceeded the number of concurrent streams. SMS Wait from previous orders. |
| API KEY not received! | Invalid API KEY has been entered |
| API KEY NOT FOUND! | Invalid API KEY has been entered |
| BANNED | User banned |
| Service NOT FOUND! | Service not found |
| UNKNOWN SERVICE OR COUNTRY | Service or country not found |

[](https://docs.smspva.com/#tag/activation_errors/Important-recommendations)Important recommendations
=====================================================================================================

**You can find APIKEY on the website in the top right drop-down menu in the Profile and APIKEY section**
--------------------------------------------------------------------------------------------------------\
If you haven't received SMS within 580 seconds (9 minutes 40 seconds), make sure to ban the number you've got.

If you ban the number when 10 minutes expired, the number you got won't be banned and might be given once again since the system keeps request ID in the base for 10 minute, after that ID is deleted from the base.

Up to 40 connections are allowed per minute.

Do interval of 4 - 5 seconds between any queries! Otherwise, you will not be able to fully use the API, because Your requests will be rejected by the server!.