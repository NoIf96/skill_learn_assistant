import * as API from '../../../'
import * as PrefixBase from '../system'

let base = PrefixBase.getBase() + 'config/';

export default {
  getModelParamOptions: params => {
    return API.GET(base + 'get_model_param_options', params);
  },
  getModelParam: params => {
    return API.GET(base + 'get_model_param', params);
  },
  generateModel: params => {
    return API.POST(base + 'generate_model', params);
  },
  saveModel: params => {
    return API.POST(base + 'save_model', params);
  },
  loadModel: params => {
    return API.POST(base + 'load_model', params);
  },
  getModelList: params => {
    return API.GET(base + 'get_model_list', params);
  },
  getImgData: params => {
    return API.GET(base + 'get_img_data', params);
  }
}
