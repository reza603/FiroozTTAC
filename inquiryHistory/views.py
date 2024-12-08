from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication  # Correct import
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
import json
import logging
import hashlib
import datetime
from barcode.models  import Inspection,ScanLogs,WarehouseOrders
from .models import Company, Product, Barcode, CustomUser
from .serializers import InspectionSerializer

logger = logging.getLogger(__name__)

# User inspection list API view with JWT Authentication
class UserInspectionListAPIView(ListAPIView):
    serializer_class = InspectionSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        logger.debug(f'Authenticated user: {user}')
        if user and user.is_authenticated:
            return Inspection.objects.filter(user=user)
        else:
            return Inspection.objects.none()

# View for handling inspection UUID queries
class InspectionUUIDView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        uuid = request.query_params.get('item')
        user = request.user.id
        print("UUID:", uuid)
        print("User ID:", user)

        if len(uuid) == 20: 
            scanloginstance = ScanLogs.objects.filter(uuid=uuid).first()
            if scanloginstance:
                whorderinstance = get_object_or_404(WarehouseOrders, orderid=scanloginstance.whorderid)
                companyinstance = get_object_or_404(Company, NationalId=whorderinstance.DistributerCompanyNid)
                product = get_object_or_404(Product, gtin=whorderinstance.GTIN)
                inspectionJson = []
                companies = []

                scanlogsAlls = ScanLogs.objects.filter(uid=uuid).order_by('updatedAt')
                for scanlogsAll in scanlogsAlls:
                    whorderinstance = get_object_or_404(WarehouseOrders, orderid=scanloginstance.whorderid)
                    companyinstance = get_object_or_404(Company, NationalId=whorderinstance.DistributerCompanyNid)
                    company_data = {
                        "company": {
                            "name": companyinstance.CompanyFaName,
                            "nid": companyinstance.NationalId,
                            "tel": companyinstance.phone,
                            "address": companyinstance.address
                        }
                    }
                    companies.append(company_data)

                CustomUserinstance = get_object_or_404(CustomUser, id=user)
                order_data = {
                    "Order": {
                        # "id": whorderinstance.id,
                        # "mfg": whorderinstance.mfg,
                        # "exp": whorderinstance.exp,
                        # "lot": whorderinstance.lot,
                        # "product": {
                        # "irc": product.irc,
                        # "gtin": product.gtin,
                        # "name": product.name
                    }
                }

                userdata = {
                    "user": {
                        "id": CustomUserinstance.id,
                        "fname": CustomUserinstance.fname,
                        "lname": CustomUserinstance.lname,
                        "mobile": CustomUserinstance.mobile,
                        "username": CustomUserinstance.username
                    }
                }

                uiddate = {"date": str(datetime.datetime.now())}
                inspectionJson.append(order_data)
                inspectionJson.append(userdata)
                inspectionJson.append(uiddate)
                inspectionJson.append(companies)
                order_json = json.dumps(inspectionJson)
                return HttpResponse(order_json, content_type="application/json")
            else:
                error = {
                    "code": "404",
                    "msg": "not found, there is no uid with this value: " + uuid
                }
                return HttpResponse(json.dumps(error), content_type="application/json")
        else:
            error = {
                "code": "404",
                "msg": "structure error on uid (must be 20 digits).==>" + uuid
            }
            return HttpResponse(json.dumps(error), content_type="application/json")

# View for showing the inquiry form
def show_inquiry_form(request):
    item = {}
    return render(request, 'inquiryHistory/inquiry.html', {'item': item})

# Function for UUID inquiry
def uuidInquiry(request):
    if request.GET.get('isuid') == 'yes':
        item = {}
        uuid = request.GET.get('item', None)
        row = Barcode.objects.filter(UUID=uuid).first()
        if row:
            item = {'uuid': row.UUID}
            data = {'items': item}
        else:
            item = {'uuid': ''}
            data = {'items': item}

        return JsonResponse(data)

# Function for RndEsalat inquiry
def RndEsalatInquiry(request):
    if request.GET.get('isuid') == 'no':
        vitem = {}
        rndesalat = request.GET.get('item', None)
        rndesalat = hashlib.sha1(rndesalat.encode('utf-8')).hexdigest().upper()
        row = Barcode.objects.filter(RndEsalat=rndesalat).first()
        if row:
            item = {'uuid': row.RndEsalat}
            data = {'items': item}
        else:
            item = {'uuid': ''}
            data = {'items': item}

        return JsonResponse(data)

# Function to handle RndEsalat inquiry via SMS
def RndEsalatInquirySMS(rndesalat, frm):
    result = ""
    if len(rndesalat) == 20:
        row = Barcode.objects.filter(UUID=rndesalat).first()
        if row:
            result = "ok"
        else:
            result = "len"
    return result

# Function to handle incoming SMS inquiries
def getSMS(request):
    udh = str(request.GET.get('udh'))
    frm = str(request.GET.get('from'))
    text = str(request.GET.get('text'))

    rndesalat = RndEsalatInquirySMS(text, frm)
    if rndesalat == "ok":
        text = "اصالت کالا مورد تایید است"
    elif rndesalat == "len":
        text = "طول کد ارسالی نامعتبر است"
    else:
        text = "اصالت کالا مورد تایید نیست"
    
    sendSmsViaGet(text, frm)
    return HttpResponse(text)

# Function to send SMS
def sendSMS(text, to):
    url = "https://sms.magfa.com/api/http/sms/v2/send"
    headers = {'accept': "application/json", 'cache-control': "no-cache"}

    username = "hamgam_611"
    password = "DQT7VCZXTLPpHZTz"
    domain = "magfa"

    payload_json = {'senders': ['3000611'], 'messages': [text], 'recipients': [to]}
    response = requests.post(url, headers=headers, auth=(username + '/' + domain, password), json=payload_json)
    print(response.json())

# Function to send SMS via GET request
def sendSmsViaGet(text, frm):
    username = "hamgam_611"
    password = "DQT7VCZXTLPpHZTz"
    domain = "magfa"

    requests.get("https://sms.magfa.com/api/http/sms/v1?service=enqueue&username=" + username + "&password=" + password + "&domain=" + domain + "&from=983000611&to=" + frm + "&text=" + text)

# Function to get SMS status
def getstatuse(request):
    mid = 12345
    url = "https://sms.magfa.com/api/http/sms/v2/statuses/" + str(mid)
    headers = {'accept': "application/json", 'cache-control': "no-cache"}

    username = "hamgam_611"
    password = "AjMvGHQJ5eFCNAC"
    domain = "magfa"

    response = requests.get(url, headers=headers, auth=(username + '/' + domain, password))
    print(response.json())
