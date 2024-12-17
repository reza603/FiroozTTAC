import json  
import datetime  
import logging  
import  requests
from django.shortcuts import get_object_or_404  ,render
from django.http import JsonResponse  
from rest_framework.permissions import IsAuthenticated  
from rest_framework.views import APIView  
from barcode.models import ScanLog  ,Barcode
from account.models import WarehouseOrder  
from products.models import Product  
from companies.models import Company  
from order.models import Order  
logger = logging.getLogger(__name__)  

class InspectionUUIDAPIView(APIView):  
    permission_classes = [IsAuthenticated]  

    def get(self, request):  
        uuid = request.GET.get('item')  
        taskid = request.GET.get('taskid')  
        logger.debug(f'Received uuid: {uuid}')  

        # Validate UUID  
        if not self.is_valid_uuid(uuid):  
            return self.error_response("Structure error on uuid (must be 20 digits)", 404)  

        # Retrieve ScanLog instance  
        scanloginstance = ScanLog.objects.filter(uuid=uuid).first()  
        logger.debug(f'scanloginstance: {scanloginstance}') 
        if not scanloginstance:  
             return self.error_response(f"Not found, there is no uuid with this value: {uuid}", 404)  

        # Collect company data  
        companies = self.get_companies(uuid,scanloginstance)  

        # Retrieve related Order and Product instances  
        order_instance = get_object_or_404(Order, OrderCode=scanloginstance.orderid)  
        product_instance = get_object_or_404(Product, gtin=order_instance.ProductCode)  
        user = request.user  

        # Construct and return the inspection JSON response  
        inspection_json = self.construct_inspection_json(order_instance, product_instance, user, companies)  
        return JsonResponse(inspection_json, status=200)  
    def mark_task_done(request):
      user = request.user
      inspection = get_object_or_404(Inspection, uuid=uuid)
      inspection.done = True
      inspection.save()
      return redirect('some_view_name')  # Redirect to a relevant page after updating
    def is_valid_uuid(self, uuid):  
      
             return uuid and len(uuid) == 20  

    def error_response(self, message, status):  
 
            error = {  
            "code": str(status),  
            "msg": message  
            }  
            return JsonResponse(error, status=status)  

    def get_companies(self, uuid,scanloginstance):  
            companies = []  
            
            company_data = {  
            "company": {  
            "name": 'گروه بهداشتی فیروز',
            "nid": '10100651897',  
            "tel": '۴۴۲۰۵۴۲۶-۴ -۰۲۱ | ۰۲۱-۴۴۲۳۶۲۵۲-۴ واحد صادرات: ۰۲۱۴۴۲۳۶۲۵۲ داخلی ۲۴۳',  
            "address":'قزوین، شهرصنعتی البرز٬ حکمت هشتم٬ شرکت گروه بهداشتی فیروز'  ,
            "scanDate":scanloginstance.createdAt.strftime("%Y-%m-%d %H:%M:%S")
            }  
            }  
            companies.append(company_data)  
            scanlogs_all = ScanLog.objects.filter(uuid=uuid).order_by('createdAt')  
            logger.warning(f" scanlogs_all: {scanlogs_all.count()}")  

            for scanlog in scanlogs_all:  
                logger.warning(f" scanlog: {scanlog.whOrderId}")  
                if scanlog.whOrderId:  
                     whorderinstance = WarehouseOrder.objects.filter(OrderId=scanlog.whOrderId, ordertype="outgoing").first()  
                     logger.warning(f" whorderinstance: {whorderinstance}")  

                    # Check if the WarehouseOrder instance was found  
                     if whorderinstance:  
                    # Retrieve the company instance  
                        company_instance = get_object_or_404(Company, national_id=whorderinstance.DistributerCompanyNid)  
                        logger.warning(f" company_instance: {company_instance}")  

                        company_data = {  
                        "company": {  
                        "name": company_instance.company_fa_name,  
                        "nid": company_instance.national_id,  
                        "tel": company_instance.phone,  
                        "address": company_instance.address  ,
                        "scanDate":scanlog.createdAt.strftime("%Y-%m-%d %H:%M:%S")
                        }  
                        }  
                        companies.append(company_data)  
                     else:  
                    # Optional: Log the missing outgoing order  
                        logger.warning(f"No outgoing warehouse order found for ScanLog ID: {scanlog.id} with whOrderId: {scanlog.whOrderId}")  
                        
                else:  
                        # Optional: Log cases where whOrderId is None  
                        logger.warning(f"ScanLog ID: {scanlog.id} does not have a valid whOrderId.")  

            return companies

    def construct_inspection_json(self, order_instance, product_instance, user, companies):  
      return {  
      "Order": {  
      "id": order_instance.OrderCode,  
      "mfg": order_instance.ProduceDate,  
      "exp": order_instance.ExpDate,  
      "lot": order_instance.BatchNumber,  
      "product": {  
      "irc": product_instance.irc,  
      "gtin": product_instance.gtin,  
      "name": product_instance.product_fr_name  
      }  
      },  
      "user": {  
      "id": user.id,  
      "fname": user.fname,  
      "lname": user.lname,  
      "mobile": user.mobile,  
      "username": user.username  
      },  
      "date": str(datetime.datetime.now()),  
      "companies": companies  
      }

def show_inquiry_form(request):
      item={}    
      return render( request,'inquiryHistory/inquiry.html',{'item': item})
def uuidInquiryToInspection(request):
       if request.GET.get('isuid')=='yes'  :
         item={}  
         row=[]
         Order_row=[]
         orderXml_row=[]
         product_row=[]
         company_row=[]
         user_row=[]
         
         uuid = request.GET.get('item', None)[6:20]  
         print(uuid)
         row=Barcode.objects.filter(UUID=uuid).first()
         if row  :
              Order_row=tblOrder.objects.filter(orderid=row.tblOrder).first()
              Orderxml_row=tblOrder.objects.filter(id=Order_row.invoicenumber).first()
              product_row=Product.objects.filter(GTIN=Order_row.gtin).first()
              company_row=Company.objects.filter(nid=Orderxml_row.oc).first()
              user_row=CustomUser.objects.filter(id=Orderxml_row.user).first()
              [{"id":"452577",
  "uid":"21996000013398957740",
  "Order":{"id":"452578","mfg":"2005-07-22","exp":"1991-03-15","lot":"58073",
  "product":{"id":"452579","gtin":"68381196592651","name":"RIENZI"}},
  "from":{"id":"452495","name":"Mae Richie","nid":"46122682651","address":"1250 Whitewater, Kaneohe, Georgia, 65340","phone":"+968-6649-885-125","mobile":"+504-6767-942-487",
  "location":{"id":"452496","latitude":"65.0243","longitude":"-88.4420"}},
  "to":{"id":"452499","name":"Celina Easley","nid":"69027369802","address":"6112 Edgars, Springfield, Indiana, 72993","phone":"+32-8755-762-980","mobile":"+501-4437-652-506",
  "location":{"id":"452500","latitude":"51.2454","longitude":"35.5409"}},
  "user":{"id":"452494","fname":"Leeann","lname":"Strong","mobile":"+92-9288-032-156","username":"erma.mcmillan2940@anyone.com","password":"friend"},"date":"2022-04-17 17:56:10"}]
              
              item={
                'uuid':row.UUID
                
              }
              data={
                'items':item
              }
         else :  
            item={
                'uuid':''
              }
            data={
                'items':item
              }       
         
         return JsonResponse(data)    
# def uuidInquiry(request):
        
#        if request.GET.get('isuid')=='yes'  :
#          item={}  
#          row=[]
#          uuid = request.GET.get('item', None)   
#          row=Barcode.objects.filter(UUID=uuid).first()
#          if row  :
            
#               item={
#                 'uuid':row.UUID
#               }
#               data={
#                 'items':item
#               }
#          else :  
#             item={
#                 'uuid':''
#               }
#             data={
#                 'items':item
#               }       
         
#          return JsonResponse(data)        
def RndEsalatInquiry(request):
     if request.GET.get('isuid')=='no' :
         vitem={}  
         row=[]
         rndesalat = request.GET.get('item', None)  
         rndesalat=  hashlib.sha1(rndesalat.encode('utf-8')).hexdigest().upper()
         row=Barcode.objects.filter(RndEsalat=rndesalat).first()
         if row :
              item={
                'uuid':row.RndEsalat
              }
              data={
                'items':item
              }
         else :  
            item={
                'uuid':''
              }
            data={
                'items':item
              }  
         
         return JsonResponse(data)   
def RndEsalatInquirySMS(rndesalat,frm):
     result=""
     if len(rndesalat)==20 :
        # rndesalat=hashlib.sha1(rndesalat.encode('utf-8')).hexdigest().upper()      
         row=Barcode.objects.filter(UUID=rndesalat).first()
         if row :
           result="ok"
         else:
           result="len"
     return result            
def getSMS(request):
    
    udh = str(request.GET.get('udh'))
    frm = str(request.GET.get('from'))
    text = str(request.GET.get('text'))
       # list=text.split("*")
    # if len(list)== 4:
    #     name=list[0]
    #     location=list[1]
    #     job=list[2]
    #     HC=list[3]
        #HC= hashlib.sha1(rndesalat.encode('utf-8')).hexdigest().upper()
        
    rndesalat=RndEsalatInquirySMS(text,frm)
    print(rndesalat)
    if rndesalat =="ok" :
        text="اصالت کالا مورد تایید است"
    elif rndesalat =="len" :  
        text="طول کد ارسالی نامعتبر است"
    else:
         text="اصالت کالا مورد تایید نیست"    
         endSmsViaGet (text,frm)
         return HttpResponse(text )
def sendSMS(text,to):
    #
    # Python samples are made with Requests: HTTP for Humans
    #
    # https://requests.readthedocs.io/en/master/
    #
    url = "https://sms.magfa.com/api/http/sms/v2/send"
    headers = {'accept': "application/json", 'cache-control': "no-cache"}
    # credentials
    username = "hamgam_611"
    password = "DQT7VCZXTLPpHZTz"
              #"AjMvGHQJ5eFCNAC"
    domain = "magfa"

    # data
    #  payload_tuples = [('senders': '3000611'), ( 'messages':text),( 'recipients':to)]
   
    # call post form data
    
    # response = requests.post(url, headers=headers, auth=(username + '/' + domain, password), data=payload_tuples)

    # or json data
    payload_json = {'senders': ['3000611'], 'messages':[text], 'recipients':[to],}
    # call json
    response = requests.post(url, headers=headers, auth=(username + '/' + domain, password), json=payload_json)
    print(response.json())
def sendSmsViaGet(text,frm):
  # https://requests.readthedocs.io/en/master/
    # credentials
  username = "hamgam_611"
  password = "DQT7VCZXTLPpHZTz"
              #"AjMvGHQJ5eFCNAC"
  domain = "magfa"

  # call
  contents = requests.get("https://sms.magfa.com/api/http/sms/v1?service=enqueue&username=" + username + "&password=" + password + "&domain=" + domain + "&from=983000611&to="+frm+"&text="+text);
def getstatuse(request):
    #
    # Python samples are made with Requests: HTTP for Humans
    #
    # https://requests.readthedocs.io/en/master/
    #
  

    mid = 12345
    url = "https://sms.magfa.com/api/http/sms/v2/statuses/" + mid
    headers = {'accept': "application/json", 'cache-control': "no-cache"}

    username = "hamgam_611"
    password = "AjMvGHQJ5eFCNAC"
    # "1@2345678"
    # AjMvGHQJ5eFCNAC
    domain = "magfa"

    # call
    response = request.get(url, headers=headers, auth=(username + '/' + domain, password))
    print(response.json())

