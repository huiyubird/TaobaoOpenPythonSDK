#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@authors: 
@date: Jun 4, 2012 8:24:36 PM
@contact: wuliang@maimiaotech.com
@version: 0.0.0
@deprecated:
@license:
@copyright:
"""

from LogisticsOrdersGetRequest import LogisticsOrdersGetRequest
from PictureIsreferencedGetRequest import PictureIsreferencedGetRequest
from InventoryAuthorizeGetallRequest import InventoryAuthorizeGetallRequest
from LogisticsPartnersGetRequest import LogisticsPartnersGetRequest
from FenxiaoLoginUserGetRequest import FenxiaoLoginUserGetRequest
from SellercatsListUpdateRequest import SellercatsListUpdateRequest
from SkusCustomGetRequest import SkusCustomGetRequest
from FenxiaoDistributorsGetRequest import FenxiaoDistributorsGetRequest
from InventoryInitialItemRequest import InventoryInitialItemRequest
from LibabaLogisticsRouteQueryRequest import LibabaLogisticsRouteQueryRequest
from ScitemMapAddRequest import ScitemMapAddRequest
from InventoryAuthorizeGetRequest import InventoryAuthorizeGetRequest
from ItemSkuUpdateRequest import ItemSkuUpdateRequest
from TopatsTasksGetRequest import TopatsTasksGetRequest
from IncrementCustomersGetRequest import IncrementCustomersGetRequest
from FenxiaoProductUpdateRequest import FenxiaoProductUpdateRequest
from LogisticsConsignResendRequest import LogisticsConsignResendRequest
from FenxiaoDiscountAddRequest import FenxiaoDiscountAddRequest
from ItemSkuPriceUpdateRequest import ItemSkuPriceUpdateRequest
from SimbaCreativesGetRequest import SimbaCreativesGetRequest
from FenxiaoProductImageUploadRequest import FenxiaoProductImageUploadRequest
from ItemAddRequest import ItemAddRequest
from WangwangEserviceNoreplynumGetRequest import WangwangEserviceNoreplynumGetRequest
from SimbaRptDemographicbaseGetRequest import SimbaRptDemographicbaseGetRequest
from InventoryQueryRequest import InventoryQueryRequest
from SimbaRptAdgroupkeywordbaseGetRequest import SimbaRptAdgroupkeywordbaseGetRequest
from IncrementCustomerPermitRequest import IncrementCustomerPermitRequest
from ScitemQueryRequest import ScitemQueryRequest
from TradeGetRequest import TradeGetRequest
from ProductGetRequest import ProductGetRequest
from ProductImgDeleteRequest import ProductImgDeleteRequest
from SubuserEmployeeUpdateRequest import SubuserEmployeeUpdateRequest
from RefundGetRequest import RefundGetRequest
from PromotionMealGetRequest import PromotionMealGetRequest
from SimbaInsightCatsGetRequest import SimbaInsightCatsGetRequest
from FenxiaoOrderCustomfieldUpdateRequest import FenxiaoOrderCustomfieldUpdateRequest
from SkusQuantityUpdateRequest import SkusQuantityUpdateRequest
from SimbaKeywordsGetRequest import SimbaKeywordsGetRequest
from PictureCategoryUpdateRequest import PictureCategoryUpdateRequest
from TraderateAddRequest import TraderateAddRequest
from InventoryAuthorizeRemoveRequest import InventoryAuthorizeRemoveRequest
from SimbaKeywordsPricevonSetRequest import SimbaKeywordsPricevonSetRequest
from SimbaAdgroupsChangedGetRequest import SimbaAdgroupsChangedGetRequest
from PromotionCoupondetailGetRequest import PromotionCoupondetailGetRequest
from FenxiaoDiscountsGetRequest import FenxiaoDiscountsGetRequest
from LibabaLogisticsOrderChargeRequest import LibabaLogisticsOrderChargeRequest
from SimbaKeywordsChangedGetRequest import SimbaKeywordsChangedGetRequest
from PromotionCouponsGetRequest import PromotionCouponsGetRequest
from FenxiaoOrderMessageAddRequest import FenxiaoOrderMessageAddRequest
from SimbaNonsearchAllplacesGetRequest import SimbaNonsearchAllplacesGetRequest
from SubuserEmployeeAddRequest import SubuserEmployeeAddRequest
from DeliveryTemplateGetRequest import DeliveryTemplateGetRequest
from ItemTemplatesGetRequest import ItemTemplatesGetRequest
from AftersaleGetRequest import AftersaleGetRequest
from SimbaAdgroupAddRequest import SimbaAdgroupAddRequest
from FenxiaoProductcatUpdateRequest import FenxiaoProductcatUpdateRequest
from SimbaCreativeAddRequest import SimbaCreativeAddRequest
from SubuserInfoUpdateRequest import SubuserInfoUpdateRequest
from SimbaInsightCatsanalysisGetRequest import SimbaInsightCatsanalysisGetRequest
from FenxiaoTrademonitorGetRequest import FenxiaoTrademonitorGetRequest
from ProductsGetRequest import ProductsGetRequest
from ShoprecommendShopsGetRequest import ShoprecommendShopsGetRequest
from FenxiaoGradeUpdateRequest import FenxiaoGradeUpdateRequest
from SubuserDutyUpdateRequest import SubuserDutyUpdateRequest
from FuwuSaleLinkGenRequest import FuwuSaleLinkGenRequest
from FeedbackAddRequest import FeedbackAddRequest
from SimbaKeywordsRecommendGetRequest import SimbaKeywordsRecommendGetRequest
from SimbaInsightCatstopwordGetRequest import SimbaInsightCatstopwordGetRequest
from ProductAddRequest import ProductAddRequest
from SellercenterSubuserPermissionsRolesGetRequest import SellercenterSubuserPermissionsRolesGetRequest
from SimbaCreativeUpdateRequest import SimbaCreativeUpdateRequest
from SimbaAdgroupsbyadgroupidsGetRequest import SimbaAdgroupsbyadgroupidsGetRequest
from SimbaRptAdgroupbaseGetRequest import SimbaRptAdgroupbaseGetRequest
from SimbaCampaignPlatformGetRequest import SimbaCampaignPlatformGetRequest
from FenxiaoCooperationProductcatAddRequest import FenxiaoCooperationProductcatAddRequest
from SimbaCatmatchidsDeletedGetRequest import SimbaCatmatchidsDeletedGetRequest
from SimbaKeywordscatQscoreGetRequest import SimbaKeywordscatQscoreGetRequest
from SellercenterRolemembersGetRequest import SellercenterRolemembersGetRequest
from TradeShippingaddressUpdateRequest import TradeShippingaddressUpdateRequest
from SimbaAdgroupOnlineitemsvonGetRequest import SimbaAdgroupOnlineitemsvonGetRequest
from FenxiaoDistributorItemsGetRequest import FenxiaoDistributorItemsGetRequest
from SimbaInsightWordsanalysisGetRequest import SimbaInsightWordsanalysisGetRequest
from WangwangEserviceEvaluationGetRequest import WangwangEserviceEvaluationGetRequest
from MarketingTagsGetRequest import MarketingTagsGetRequest
from ScitemOutercodeGetRequest import ScitemOutercodeGetRequest
from LibabaLogisticsOrderConsignRequest import LibabaLogisticsOrderConsignRequest
from WangwangEserviceLoginlogsGetRequest import WangwangEserviceLoginlogsGetRequest
from ItemImgDeleteRequest import ItemImgDeleteRequest
from FenxiaoDiscountUpdateRequest import FenxiaoDiscountUpdateRequest
from LogisticsOfflineSendRequest import LogisticsOfflineSendRequest
from SubuserDepartmentDeleteRequest import SubuserDepartmentDeleteRequest
from PictureDeleteRequest import PictureDeleteRequest
from SimbaCreativesChangedGetRequest import SimbaCreativesChangedGetRequest
from SimbaAdgroupCampcatmatchsGetRequest import SimbaAdgroupCampcatmatchsGetRequest
from ProductPropimgUploadRequest import ProductPropimgUploadRequest
from SimbaLoginAuthsignGetRequest import SimbaLoginAuthsignGetRequest
from SimbaAdgroupCatmatchUpdateRequest import SimbaAdgroupCatmatchUpdateRequest
from FenxiaoCooperationUpdateRequest import FenxiaoCooperationUpdateRequest
from AreasGetRequest import AreasGetRequest
from ItemRecommendAddRequest import ItemRecommendAddRequest
from SimbaCampaignPlatformUpdateRequest import SimbaCampaignPlatformUpdateRequest
from FenxiaoProductcatAddRequest import FenxiaoProductcatAddRequest
from InventoryOccupyCancelRequest import InventoryOccupyCancelRequest
from ShopcatsListGetRequest import ShopcatsListGetRequest
from SimbaToolsItemsTopGetRequest import SimbaToolsItemsTopGetRequest
from LogisticsOrdertracePushRequest import LogisticsOrdertracePushRequest
from ItemsOnsaleGetRequest import ItemsOnsaleGetRequest
from PictureCategoryAddRequest import PictureCategoryAddRequest
from ShopRemainshowcaseGetRequest import ShopRemainshowcaseGetRequest
from PromotionActivityGetRequest import PromotionActivityGetRequest
from MarketingPromotionKfcRequest import MarketingPromotionKfcRequest
from SimbaAdgroupUpdateRequest import SimbaAdgroupUpdateRequest
from SimbaAdgroupChangedcatmatchsGetRequest import SimbaAdgroupChangedcatmatchsGetRequest
from InventoryAuthorizeSetRequest import InventoryAuthorizeSetRequest
from SimbaRptAdgroupkeywordeffectGetRequest import SimbaRptAdgroupkeywordeffectGetRequest
from DeliveryTemplateDeleteRequest import DeliveryTemplateDeleteRequest
from TradeSnapshotGetRequest import TradeSnapshotGetRequest
from FenxiaoProductSkusGetRequest import FenxiaoProductSkusGetRequest
from SimbaCampaignAreaoptionsGetRequest import SimbaCampaignAreaoptionsGetRequest
from InventoryAuthorizeRemoveallRequest import InventoryAuthorizeRemoveallRequest
from ItemPropimgUploadRequest import ItemPropimgUploadRequest
from SellercenterRoleAddRequest import SellercenterRoleAddRequest
from SimbaNonsearchAdgroupplacesGetRequest import SimbaNonsearchAdgroupplacesGetRequest
from WangwangEserviceStreamweigthsGetRequest import WangwangEserviceStreamweigthsGetRequest
from RefundMessageAddRequest import RefundMessageAddRequest
from MarketingPromotionsGetRequest import MarketingPromotionsGetRequest
from SimbaKeywordsvonAddRequest import SimbaKeywordsvonAddRequest
from SimbaKeywordsDeleteRequest import SimbaKeywordsDeleteRequest
from FenxiaoGradeAddRequest import FenxiaoGradeAddRequest
from SubuserDutyAddRequest import SubuserDutyAddRequest
from SimbaAccountBalanceGetRequest import SimbaAccountBalanceGetRequest
from LogisticsOnlineCancelRequest import LogisticsOnlineCancelRequest
from PictureGetRequest import PictureGetRequest
from RefundsApplyGetRequest import RefundsApplyGetRequest
from CometDiscardinfoGetRequest import CometDiscardinfoGetRequest
from FenxiaoProductPduUpdateRequest import FenxiaoProductPduUpdateRequest
from PictureUserinfoGetRequest import PictureUserinfoGetRequest
from LogisticsOnlineSendRequest import LogisticsOnlineSendRequest
from SimbaRptAdgroupcreativeeffectGetRequest import SimbaRptAdgroupcreativeeffectGetRequest
from TradeMemoUpdateRequest import TradeMemoUpdateRequest
from SimbaInsightWordsbaseGetRequest import SimbaInsightWordsbaseGetRequest
from SimbaKeywordsAddRequest import SimbaKeywordsAddRequest
from TraderatesGetRequest import TraderatesGetRequest
from ItemPropimgDeleteRequest import ItemPropimgDeleteRequest
from ItemImgUploadRequest import ItemImgUploadRequest
from ProductUpdateRequest import ProductUpdateRequest
from TradeOrderskuUpdateRequest import TradeOrderskuUpdateRequest
from ScitemMapDeleteRequest import ScitemMapDeleteRequest
from LibabaLogisticsOrderCancelRequest import LibabaLogisticsOrderCancelRequest
from SimbaRptCustbaseGetRequest import SimbaRptCustbaseGetRequest
from TopatsDeliverySendRequest import TopatsDeliverySendRequest
from MallBrandcatSalesproGetRequest import MallBrandcatSalesproGetRequest
from SimbaKeywordidsChangedGetRequest import SimbaKeywordidsChangedGetRequest
from SimbaRptAdgroupcreativebaseGetRequest import SimbaRptAdgroupcreativebaseGetRequest
from TraderateListAddRequest import TraderateListAddRequest
from SellercenterRoleInfoGetRequest import SellercenterRoleInfoGetRequest
from PictureUpdateRequest import PictureUpdateRequest
from SimbaCampaignAreaGetRequest import SimbaCampaignAreaGetRequest
from RefundMessagesGetRequest import RefundMessagesGetRequest
from FenxiaoProductImageDeleteRequest import FenxiaoProductImageDeleteRequest
from SimbaCampaignChanneloptionsGetRequest import SimbaCampaignChanneloptionsGetRequest
from FenxiaoCooperationGetRequest import FenxiaoCooperationGetRequest
from ItemcatsIncrementGetRequest import ItemcatsIncrementGetRequest
from SimbaRptAdgroupnonsearcheffectGetRequest import SimbaRptAdgroupnonsearcheffectGetRequest
from SimbaCreativeidsDeletedGetRequest import SimbaCreativeidsDeletedGetRequest
from FenxiaoCooperationAuditRequest import FenxiaoCooperationAuditRequest
from FenxiaoProductAddRequest import FenxiaoProductAddRequest
from WangwangEserviceEvalsGetRequest import WangwangEserviceEvalsGetRequest
from SimbaKeywordidsDeletedGetRequest import SimbaKeywordidsDeletedGetRequest
from LogisticsCompaniesGetRequest import LogisticsCompaniesGetRequest
from TradesSoldIncrementGetRequest import TradesSoldIncrementGetRequest
from SimbaKeywordsbyadgroupidGetRequest import SimbaKeywordsbyadgroupidGetRequest
from TradeAmountGetRequest import TradeAmountGetRequest
from SimbaCampaignAreaUpdateRequest import SimbaCampaignAreaUpdateRequest
from SimbaNonsearchAlldemographicsGetRequest import SimbaNonsearchAlldemographicsGetRequest
from TopatsIncrementMessagesGetRequest import TopatsIncrementMessagesGetRequest
from ItemJointImgRequest import ItemJointImgRequest
from PictureReplaceRequest import PictureReplaceRequest
from TradeReceivetimeDelayRequest import TradeReceivetimeDelayRequest
from FenxiaoProductcatsGetRequest import FenxiaoProductcatsGetRequest
from SimbaAdgroupCatmatchGetRequest import SimbaAdgroupCatmatchGetRequest
from InventoryAdjustTradeRequest import InventoryAdjustTradeRequest
from LogisticsDummySendRequest import LogisticsDummySendRequest
from FenxiaoProductcatDeleteRequest import FenxiaoProductcatDeleteRequest
from FenxiaoGradesGetRequest import FenxiaoGradesGetRequest
from SubuserDutysGetRequest import SubuserDutysGetRequest
from ItemsCustomGetRequest import ItemsCustomGetRequest
from TopatsItemcatsGetRequest import TopatsItemcatsGetRequest
from SellercatsListAddRequest import SellercatsListAddRequest
from SubuserDepartmentAddRequest import SubuserDepartmentAddRequest
from LogisticsAddressAddRequest import LogisticsAddressAddRequest
from ShopGetRequest import ShopGetRequest
from IncrementRefundsGetRequest import IncrementRefundsGetRequest
from ItemrecommendItemsGetRequest import ItemrecommendItemsGetRequest
from SimbaRptDemographiceffectGetRequest import SimbaRptDemographiceffectGetRequest
from ItempropsGetRequest import ItempropsGetRequest
from SimbaRptAdgroupeffectGetRequest import SimbaRptAdgroupeffectGetRequest
from ScitemUpdateRequest import ScitemUpdateRequest
from IncrementAuthorizeMessageGetRequest import IncrementAuthorizeMessageGetRequest
from UserSellerGetRequest import UserSellerGetRequest
from TimeGetRequest import TimeGetRequest
from SimbaCampaignBudgetUpdateRequest import SimbaCampaignBudgetUpdateRequest
from ItemSkuGetRequest import ItemSkuGetRequest
from ShopUpdateRequest import ShopUpdateRequest
from LogisticsOnlineConfirmRequest import LogisticsOnlineConfirmRequest
from SimbaAdgroupAdgroupcatmatchsGetRequest import SimbaAdgroupAdgroupcatmatchsGetRequest
from ProductsSearchRequest import ProductsSearchRequest
from FenxiaoOrdersGetRequest import FenxiaoOrdersGetRequest
from SellercenterRolesGetRequest import SellercenterRolesGetRequest
from ItempropvaluesGetRequest import ItempropvaluesGetRequest
from TopatsTaskDeleteRequest import TopatsTaskDeleteRequest
from SimbaNonsearchDemographicsUpdateRequest import SimbaNonsearchDemographicsUpdateRequest
from FenxiaoOrderRemarkUpdateRequest import FenxiaoOrderRemarkUpdateRequest
from SimbaRptCampaignbaseGetRequest import SimbaRptCampaignbaseGetRequest
from FenxiaoProductSkuUpdateRequest import FenxiaoProductSkuUpdateRequest
from SimbaAdgroupDeleteRequest import SimbaAdgroupDeleteRequest
from LogisticsTraceSearchRequest import LogisticsTraceSearchRequest
from InventoryInitialRequest import InventoryInitialRequest
from UserrecommendItemsGetRequest import UserrecommendItemsGetRequest
from IncrementTradesGetRequest import IncrementTradesGetRequest
from ShoprecommendItemsGetRequest import ShoprecommendItemsGetRequest
from SimbaAdgroupidsDeletedGetRequest import SimbaAdgroupidsDeletedGetRequest
from FenxiaoRequisitionsGetRequest import FenxiaoRequisitionsGetRequest
from TraderateExplainAddRequest import TraderateExplainAddRequest
from MallBrandcatControlGetRequest import MallBrandcatControlGetRequest
from PromotionLimitdiscountDetailGetRequest import PromotionLimitdiscountDetailGetRequest
from SimbaInsightCatsforecastGetRequest import SimbaInsightCatsforecastGetRequest
from SimbaAdgroupNonsearchpricesUpdateRequest import SimbaAdgroupNonsearchpricesUpdateRequest
from RefundsReceiveGetRequest import RefundsReceiveGetRequest
from FenxiaoProductGradepriceGetRequest import FenxiaoProductGradepriceGetRequest
from SimbaAdgroupNonsearchstatesUpdateRequest import SimbaAdgroupNonsearchstatesUpdateRequest
from MallProductSpecAddRequest import MallProductSpecAddRequest
from WangwangEserviceOnlinetimeGetRequest import WangwangEserviceOnlinetimeGetRequest
from TradeCloseRequest import TradeCloseRequest
from LogisticsAddressSearchRequest import LogisticsAddressSearchRequest
from SimbaAdgroupOnlineitemsGetRequest import SimbaAdgroupOnlineitemsGetRequest
from FenxiaoProductsGetRequest import FenxiaoProductsGetRequest
from SimbaCreativesRecordGetRequest import SimbaCreativesRecordGetRequest
from SimbaAdgroupDeletedcatmatchsGetRequest import SimbaAdgroupDeletedcatmatchsGetRequest
from SimbaAdgroupCatmatchforecastGetRequest import SimbaAdgroupCatmatchforecastGetRequest
from SimbaAdgroupsItemExistRequest import SimbaAdgroupsItemExistRequest
from VasOrderSearchRequest import VasOrderSearchRequest
from SimbaNonsearchAdgroupplacesUpdateRequest import SimbaNonsearchAdgroupplacesUpdateRequest
from VasSubscribeGetRequest import VasSubscribeGetRequest
from ItemRecommendDeleteRequest import ItemRecommendDeleteRequest
from SimbaCampaignUpdateRequest import SimbaCampaignUpdateRequest
from SimbaCampaignBudgetGetRequest import SimbaCampaignBudgetGetRequest
from DeliveryTemplatesGetRequest import DeliveryTemplatesGetRequest
from FenxiaoOrderConfirmPaidRequest import FenxiaoOrderConfirmPaidRequest
from SimbaAdgroupidsChangedGetRequest import SimbaAdgroupidsChangedGetRequest
from ScitemMapQueryRequest import ScitemMapQueryRequest
from SimbaInsightWordscatsGetRequest import SimbaInsightWordscatsGetRequest
from TopatsSimbaCampkeywordbaseGetRequest import TopatsSimbaCampkeywordbaseGetRequest
from SimbaCreativeDeleteRequest import SimbaCreativeDeleteRequest
from DeliveryTemplateAddRequest import DeliveryTemplateAddRequest
from SimbaAdgroupsGetRequest import SimbaAdgroupsGetRequest
from RefundRefuseRequest import RefundRefuseRequest
from ItemsInventoryGetRequest import ItemsInventoryGetRequest
from ProductImgUploadRequest import ProductImgUploadRequest
from SimbaKeywordKeywordforecastGetRequest import SimbaKeywordKeywordforecastGetRequest
from SellercenterUserPermissionsGetRequest import SellercenterUserPermissionsGetRequest
from LogisticsOrderstorePushRequest import LogisticsOrderstorePushRequest
from ItemDeleteRequest import ItemDeleteRequest
from FenxiaoOrderCloseRequest import FenxiaoOrderCloseRequest
from ScitemGetRequest import ScitemGetRequest
from FenxiaoProductSkuDeleteRequest import FenxiaoProductSkuDeleteRequest
from TopatsTradesFullinfoGetRequest import TopatsTradesFullinfoGetRequest
from ItemQuantityUpdateRequest import ItemQuantityUpdateRequest
from ItemGetRequest import ItemGetRequest
from SimbaCustomersAuthorizedGetRequest import SimbaCustomersAuthorizedGetRequest
from LogisticsOrdersDetailGetRequest import LogisticsOrdersDetailGetRequest
from SimbaAdgroupsbycampaignidGetRequest import SimbaAdgroupsbycampaignidGetRequest
from TradePostageUpdateRequest import TradePostageUpdateRequest
from ItemcatsAuthorizeGetRequest import ItemcatsAuthorizeGetRequest
from SimbaInsightCatsrelatedwordGetRequest import SimbaInsightCatsrelatedwordGetRequest
from SellercenterSubusersGetRequest import SellercenterSubusersGetRequest
from MallProductSpecPicUploadRequest import MallProductSpecPicUploadRequest
from DeliveryTemplateUpdateRequest import DeliveryTemplateUpdateRequest
from UmpPromotionGetRequest import UmpPromotionGetRequest
from SimbaKeywordsQscoreGetRequest import SimbaKeywordsQscoreGetRequest
from PictureUploadRequest import PictureUploadRequest
from ItemSkuAddRequest import ItemSkuAddRequest
from SimbaRptCampaigneffectGetRequest import SimbaRptCampaigneffectGetRequest
from FenxiaoProductSkuAddRequest import FenxiaoProductSkuAddRequest
from InventoryAdjustExternalRequest import InventoryAdjustExternalRequest
from ItemUpdateDelistingRequest import ItemUpdateDelistingRequest
from KfcKeywordSearchRequest import KfcKeywordSearchRequest
from SellercatsListGetRequest import SellercatsListGetRequest
from IncrementCustomerStopRequest import IncrementCustomerStopRequest
from ItemUpdateRequest import ItemUpdateRequest
from ItemSkusGetRequest import ItemSkusGetRequest
from WangwangEserviceGroupmemberGetRequest import WangwangEserviceGroupmemberGetRequest
from PromotionLimitdiscountGetRequest import PromotionLimitdiscountGetRequest
from ItemSkuDeleteRequest import ItemSkuDeleteRequest
from SubuserDepartmentUpdateRequest import SubuserDepartmentUpdateRequest
from TopatsSimbaCampkeywordeffectGetRequest import TopatsSimbaCampkeywordeffectGetRequest
from FenxiaoOrderCreateDealerRequest import FenxiaoOrderCreateDealerRequest
from SimbaRptCampadgroupeffectGetRequest import SimbaRptCampadgroupeffectGetRequest
from SimbaKeywordsbykeywordidsGetRequest import SimbaKeywordsbykeywordidsGetRequest
from InventoryOccupyApplyRequest import InventoryOccupyApplyRequest
from CategoryrecommendItemsGetRequest import CategoryrecommendItemsGetRequest
from ItemsListGetRequest import ItemsListGetRequest
from InventoryStoreQueryRequest import InventoryStoreQueryRequest
from ItemcatsGetRequest import ItemcatsGetRequest
from IncrementItemsGetRequest import IncrementItemsGetRequest
from SimbaNonsearchAdgroupplacesAddRequest import SimbaNonsearchAdgroupplacesAddRequest
from LogisticsAddressRemoveRequest import LogisticsAddressRemoveRequest
from SimbaInsightCatsbaseGetRequest import SimbaInsightCatsbaseGetRequest
from SimbaRptCampadgroupbaseGetRequest import SimbaRptCampadgroupbaseGetRequest
from TradeConfirmfeeGetRequest import TradeConfirmfeeGetRequest
from ItemJointPropimgRequest import ItemJointPropimgRequest
from ItemPriceUpdateRequest import ItemPriceUpdateRequest
from FenxiaoOrderPayRequest import FenxiaoOrderPayRequest
from SimbaRptAdgroupnonsearchbaseGetRequest import SimbaRptAdgroupnonsearchbaseGetRequest
from SimbaNonsearchDemographicsGetRequest import SimbaNonsearchDemographicsGetRequest
from SimbaRptCusteffectGetRequest import SimbaRptCusteffectGetRequest
from FenxiaoGradeDeleteRequest import FenxiaoGradeDeleteRequest
from SubuserDutyDeleteRequest import SubuserDutyDeleteRequest
from SubuserFullinfoGetRequest import SubuserFullinfoGetRequest
from SimbaNonsearchAdgroupplacesDeleteRequest import SimbaNonsearchAdgroupplacesDeleteRequest
from WangwangEserviceAvgwaittimeGetRequest import WangwangEserviceAvgwaittimeGetRequest
from TradeMemoAddRequest import TradeMemoAddRequest
from ItemUpdateListingRequest import ItemUpdateListingRequest
from MallProductSpecGetRequest import MallProductSpecGetRequest
from TopatsTradesSoldGetRequest import TopatsTradesSoldGetRequest
from ItemAnchorGetRequest import ItemAnchorGetRequest
from ProductPropimgDeleteRequest import ProductPropimgDeleteRequest
from TradesSoldGetRequest import TradesSoldGetRequest
from InventoryStoreManageRequest import InventoryStoreManageRequest
from TradeFullinfoGetRequest import TradeFullinfoGetRequest
from SimbaCampaignsGetRequest import SimbaCampaignsGetRequest
from MallProductSpecsGetRequest import MallProductSpecsGetRequest
from LogisticsAddressModifyRequest import LogisticsAddressModifyRequest
from PictureReferencedGetRequest import PictureReferencedGetRequest
from SimbaCampaignScheduleGetRequest import SimbaCampaignScheduleGetRequest
from TradesSoldIncrementvGetRequest import TradesSoldIncrementvGetRequest
from FenxiaoCooperationTerminateRequest import FenxiaoCooperationTerminateRequest
from SimbaCampaignAddRequest import SimbaCampaignAddRequest
from SimbaCreativeidsChangedGetRequest import SimbaCreativeidsChangedGetRequest
from SimbaCatmatchidsChangedGetRequest import SimbaCatmatchidsChangedGetRequest
from ScitemAddRequest import ScitemAddRequest
from FenxiaoProductMapAddRequest import FenxiaoProductMapAddRequest
from SubuserDepartmentsGetRequest import SubuserDepartmentsGetRequest
from VasSubscSearchRequest import VasSubscSearchRequest
from SimbaKeywordsPriceSetRequest import SimbaKeywordsPriceSetRequest
from FenxiaoProductGradepriceUpdateRequest import FenxiaoProductGradepriceUpdateRequest
from SimbaCampaignScheduleUpdateRequest import SimbaCampaignScheduleUpdateRequest
from WangwangEserviceReceivenumGetRequest import WangwangEserviceReceivenumGetRequest
from SubusersGetRequest import SubusersGetRequest
from PictureCategoryGetRequest import PictureCategoryGetRequest
from SimbaInsightToplevelcatsGetRequest import SimbaInsightToplevelcatsGetRequest
from FenxiaoProductMapDeleteRequest import FenxiaoProductMapDeleteRequest
from TopatsResultGetRequest import TopatsResultGetRequest
