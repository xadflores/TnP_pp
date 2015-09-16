from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'TnP_pp_GenTrackSTA'
config.General.workArea = 'TnP_pp_GenTrackSTA_A'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'tp_pp_sta.py'

config.section_("Data")
config.Data.inputDataset = '/PPMuon/Run2013A-PromptReco-v1/RECO'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.lumiMask = 'Cert_211739-211831_2760GeV_PromptReco_Collisions13_JSON_MuonPhys.txt'
config.Data.runRange = '211739-211831'
config.Data.ignoreLocality = True
config.Data.publication = False
# This string is used to construct the output dataset name
#config.Data.publishDBS = 'phys03'
#config.Data.publishDataName = 'B2GAnaFW_V74x_V43'

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'


