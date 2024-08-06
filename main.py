import requests

url = "https://mapps.co.maui.hi.us/energov_prod/selfservice/api/energov/search/search"


for i in range(1, 101):
    payload = '''{
        "Keyword": "",
        "ExactMatch": True,
        "SearchModule": 1,
        "FilterModule": 2,
        "SearchMainAddress": False,
        "PlanCriteria": {
            "PlanNumber": None,
            "PlanTypeId": None,
            "PlanWorkclassId": None,
            "PlanStatusId": None,
            "ProjectName": None,
            "ApplyDateFrom": None,
            "ApplyDateTo": None,
            "ExpireDateFrom": None,
            "ExpireDateTo": None,
            "CompleteDateFrom": None,
            "CompleteDateTo": None,
            "Address": None,
            "Description": None,
            "SearchMainAddress": False,
            "ContactId": None,
            "ParcelNumber": None,
            "TypeId": None,
            "WorkClassIds": None,
            "ExcludeCases": None,
            "EnableDescriptionSearch": False,
            "PageNumber": 0,
            "PageSize": 0,
            "SortBy": None,
            "SortAscending": False
        },
        "PermitCriteria": {
            "PermitNumber": None,
            "PermitTypeId": None,
            "PermitWorkclassId": None,
            "PermitStatusId": None,
            "ProjectName": None,
            "IssueDateFrom": None,
            "IssueDateTo": None,
            "Address": None,
            "Description": None,
            "ExpireDateFrom": None,
            "ExpireDateTo": None,
            "FinalDateFrom": None,
            "FinalDateTo": None,
            "ApplyDateFrom": None,
            "ApplyDateTo": None,
            "SearchMainAddress": False,
            "ContactId": None,
            "TypeId": None,
            "WorkClassIds": None,
            "ParcelNumber": None,
            "ExcludeCases": None,
            "EnableDescriptionSearch": False,
            "PageNumber": 0,
            "PageSize": 0,
            "SortBy": "FinalDate",
            "SortAscending": False
        },
        "InspectionCriteria": {
            "Keyword": None,
            "ExactMatch": False,
            "Complete": None,
            "InspectionNumber": None,
            "InspectionTypeId": None,
            "InspectionStatusId": None,
            "RequestDateFrom": None,
            "RequestDateTo": None,
            "ScheduleDateFrom": None,
            "ScheduleDateTo": None,
            "Address": None,
            "SearchMainAddress": False,
            "ContactId": None,
            "TypeId": [],
            "WorkClassIds": [],
            "ParcelNumber": None,
            "DisplayCodeInspections": False,
            "ExcludeCases": [],
            "ExcludeFilterModules": [],
            "HiddenInspectionTypeIDs": None,
            "PageNumber": 0,
            "PageSize": 0,
            "SortBy": None,
            "SortAscending": False
        },
        "CodeCaseCriteria": {
            "CodeCaseNumber": None,
            "CodeCaseTypeId": None,
            "CodeCaseStatusId": None,
            "ProjectName": None,
            "OpenedDateFrom": None,
            "OpenedDateTo": None,
            "ClosedDateFrom": None,
            "ClosedDateTo": None,
            "Address": None,
            "ParcelNumber": None,
            "Description": None,
            "SearchMainAddress": False,
            "RequestId": None,
            "ExcludeCases": None,
            "ContactId": None,
            "EnableDescriptionSearch": False,
            "PageNumber": 0,
            "PageSize": 0,
            "SortBy": None,
            "SortAscending": False
        },
        "RequestCriteria": {
            "RequestNumber": None,
            "RequestTypeId": None,
            "RequestStatusId": None,
            "ProjectName": None,
            "EnteredDateFrom": None,
            "EnteredDateTo": None,
            "DeadlineDateFrom": None,
            "DeadlineDateTo": None,
            "CompleteDateFrom": None,
            "CompleteDateTo": None,
            "Address": None,
            "ParcelNumber": None,
            "SearchMainAddress": False,
            "PageNumber": 0,
            "PageSize": 0,
            "SortBy": None,
            "SortAscending": False
        },
        "BusinessLicenseCriteria": {
            "LicenseNumber": None,
            "LicenseTypeId": None,
            "LicenseClassId": None,
            "LicenseStatusId": None,
            "BusinessStatusId": None,
            "LicenseYear": None,
            "ApplicationDateFrom": None,
            "ApplicationDateTo": None,
            "IssueDateFrom": None,
            "IssueDateTo": None,
            "ExpirationDateFrom": None,
            "ExpirationDateTo": None,
            "SearchMainAddress": False,
            "CompanyTypeId": None,
            "CompanyName": None,
            "BusinessTypeId": None,
            "Description": None,
            "CompanyOpenedDateFrom": None,
            "CompanyOpenedDateTo": None,
            "CompanyClosedDateFrom": None,
            "CompanyClosedDateTo": None,
            "LastAuditDateFrom": None,
            "LastAuditDateTo": None,
            "ParcelNumber": None,
            "Address": None,
            "TaxID": None,
            "DBA": None,
            "ExcludeCases": None,
            "TypeId": None,
            "WorkClassIds": None,
            "ContactId": None,
            "PageNumber": 0,
            "PageSize": 0,
            "SortBy": None,
            "SortAscending": False
        },
        "ProfessionalLicenseCriteria": {
            "LicenseNumber": None,
            "HolderFirstName": None,
            "HolderMiddleName": None,
            "HolderLastName": None,
            "HolderCompanyName": None,
            "LicenseTypeId": None,
            "LicenseClassId": None,
            "LicenseStatusId": None,
            "IssueDateFrom": None,
            "IssueDateTo": None,
            "ExpirationDateFrom": None,
            "ExpirationDateTo": None,
            "ApplicationDateFrom": None,
            "ApplicationDateTo": None,
            "Address": None,
            "MainParcel": None,
            "SearchMainAddress": False,
            "ExcludeCases": None,
            "TypeId": None,
            "WorkClassIds": None,
            "ContactId": None,
            "PageNumber": 0,
            "PageSize": 0,
            "SortBy": None,
            "SortAscending": False
        },
        "LicenseCriteria": {
            "LicenseNumber": None,
            "LicenseTypeId": None,
            "LicenseClassId": None,
            "LicenseStatusId": None,
            "BusinessStatusId": None,
            "ApplicationDateFrom": None,
            "ApplicationDateTo": None,
            "IssueDateFrom": None,
            "IssueDateTo": None,
            "ExpirationDateFrom": None,
            "ExpirationDateTo": None,
            "SearchMainAddress": False,
            "CompanyTypeId": None,
            "CompanyName": None,
            "BusinessTypeId": None,
            "Description": None,
            "CompanyOpenedDateFrom": None,
            "CompanyOpenedDateTo": None,
            "CompanyClosedDateFrom": None,
            "CompanyClosedDateTo": None,
            "LastAuditDateFrom": None,
            "LastAuditDateTo": None,
            "ParcelNumber": None,
            "Address": None,
            "TaxID": None,
            "DBA": None,
            "ExcludeCases": None,
            "TypeId": None,
            "WorkClassIds": None,
            "ContactId": None,
            "HolderFirstName": None,
            "HolderMiddleName": None,
            "HolderLastName": None,
            "MainParcel": None,
            "EnableDescriptionSearchForBLicense": False,
            "EnableDescriptionSearchForPLicense": False,
            "PageNumber": 0,
            "PageSize": 0,
            "SortBy": None,
            "SortAscending": False
        },
        "ProjectCriteria": {
            "ProjectNumber": None,
            "ProjectName": None,
            "Address": None,
            "ParcelNumber": None,
            "StartDateFrom": None,
            "StartDateTo": None,
            "ExpectedEndDateFrom": None,
            "ExpectedEndDateTo": None,
            "CompleteDateFrom": None,
            "CompleteDateTo": None,
            "Description": None,
            "SearchMainAddress": False,
            "ContactId": None,
            "TypeId": None,
            "ExcludeCases": None,
            "EnableDescriptionSearch": False,
            "PageNumber": 0,
            "PageSize": 0,
            "SortBy": None,
            "SortAscending": False
        },
        "PlanSortList": [
            {
                "Key": "relevance",
                "Value": "Relevance"
            },
            {
                "Key": "PlanNumber.keyword",
                "Value": "Plan Number"
            },
            {
                "Key": "ProjectName.keyword",
                "Value": "Project"
            },
            {
                "Key": "MainAddress",
                "Value": "Address"
            },
            {
                "Key": "ApplyDate",
                "Value": "Apply Date"
            }
        ],
        "PermitSortList": [
            {
                "Key": "relevance",
                "Value": "Relevance"
            },
            {
                "Key": "PermitNumber.keyword",
                "Value":
    
     "Permit Number"
            },
            {
                "Key": "ProjectName.keyword",
                "Value": "Project"
            },
            {
                "Key": "MainAddress",
                "Value": "Address"
            },
            {
                "Key": "IssueDate",
                "Value": "Issued Date"
            },
            {
                "Key": "FinalDate",
                "Value": "Finalized Date"
            }
        ],
        "InspectionSortList": [
            {
                "Key": "relevance",
                "Value": "Relevance"
            },
            {
                "Key": "InspectionNumber.keyword",
                "Value": "Inspection Number"
            },
            {
                "Key": "MainAddress",
                "Value": "Address"
            },
            {
                "Key": "ScheduledDate",
                "Value": "Schedule Date"
            },
            {
                "Key": "RequestDate",
                "Value": "Request Date"
            }
        ],
        "CodeCaseSortList": [
            {
                "Key": "relevance",
                "Value": "Relevance"
            },
            {
                "Key": "CaseNumber.keyword",
                "Value": "Code Case Number"
            },
            {
                "Key": "ProjectName.keyword",
                "Value": "Project"
            },
            {
                "Key": "MainAddress",
                "Value": "Address"
            },
            {
                "Key": "OpenedDate",
                "Value": "Opened Date"
            },
            {
                "Key": "ClosedDate",
                "Value": "Closed Date"
            }
        ],
        "RequestSortList": [
            {
                "Key": "relevance",
                "Value": "Relevance"
            },
            {
                "Key": "RequestNumber.keyword",
                "Value": "Request Number"
            },
            {
                "Key": "ProjectName.keyword",
                "Value": "Project Name"
            },
            {
                "Key": "MainAddress",
                "Value": "Address"
            },
            {
                "Key": "EnteredDate",
                "Value": "Date Entered"
            },
            {
                "Key": "CompleteDate",
                "Value": "Completion Date"
            }
        ],
        "LicenseSortList": [
            {
                "Key": "relevance",
                "Value": "Relevance"
            },
            {
                "Key": "LicenseNumber.keyword",
                "Value": "License Number"
            },
            {
                "Key": "CompanyName.keyword",
                "Value": "Company Name"
            },
            {
                "Key": "AppliedDate",
                "Value": "Applied Date"
            },
            {
                "Key": "MainAddress",
                "Value": "Address"
            }
        ],
        "ProjectSortList": [
            {
                "Key": "relevance",
                "Value": "Relevance"
            },
            {
                "Key": "ProjectNumber.keyword",
                "Value": "Project Number"
            },
            {
                "Key": "ProjectName.keyword",
                "Value": "Project Name"
            },
            {
                "Key": "StartDate",
                "Value": "Start Date"
            },
            {
                "Key": "CompleteDate",
                "Value": "Completed Date"
            },
            {
                "Key": "ExpectedEndDate",
                "Value": "Expected End Date"
            },
            {
                "Key": "MainAddress",
                "Value": "Address"
            }
        ],
        "ExcludeCases": None,
        "SortOrderList": [
            {
                "Key": True,
                "Value": "Ascending"
            },
            {
                "Key": False,
                "Value": "Descending"
            }
        ],
        "HiddenInspectionTypeIDs": None,
        "PageNumber": {0},
        "PageSize": 100,
        "SortBy": "FinalDate",
        "SortAscending": False
    }'''

    payload.format(i)

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'Tyler-Tenant-Culture=en-US',
        'Origin': 'https://mapps.co.maui.hi.us',
        'Referer': 'https://mapps.co.maui.hi.us/EnerGov_Prod/SelfService',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'Tyler-Tenant-Culture': 'en-US',
        'Tyler-TenantUrl': 'MauiCountyHIProd',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'tenantId': '1',
        'tenantName': 'MauiCountyHIProd'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)

