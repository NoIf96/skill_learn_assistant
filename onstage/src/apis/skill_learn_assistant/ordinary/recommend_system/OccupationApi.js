import * as API from '../../../'
import * as PrefixBase from '../recommend_system'

let base = PrefixBase.getBase() + 'occupation/';

export default {
  getRecommendedOccupationList: params => {
    return API.GET(base + 'get_recommended_occupation_list');
  },
  addUserRecommendOccupationList: params => {
    return API.POST(base + 'add_user_recommend_occupation_list', params);
  }
}
