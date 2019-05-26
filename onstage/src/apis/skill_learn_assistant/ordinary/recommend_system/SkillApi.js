import * as API from '../../../'
import * as PrefixBase from '../recommend_system'

let base = PrefixBase.getBase() + 'skill/';

export default {
  getRecommendedSkillTree: params => {
    return API.GET(base + 'get_recommended_skill_tree');
  },
  getAddUserSkill: params => {
    return API.POST(base + 'add_user_skill', params);
  }
}
