import * as API from '../../../'
import * as PrefixBase from '../library'

let base = PrefixBase.getBase() + 'skill/';

export default {
  add: params => {
    return API.POST(base + 'add', params);
  },
  del: params => {
    return API.POST(base + 'delete', params);
  },
  edit: params => {
    return API.POST(base + 'edit', params);
  },
  getList: params => {
    return API.GET(base + 'list', params);
  },
  getSortOptions: params => {
    return API.GET(base + 'get_sort_options', params);
  },
  autoUpdateSkillIntroduction: params => {
    return API.GET(base + 'auto_update_skill_introduction', params);
  },
  getSkillIntroduction: params => {
    return API.POST(base + 'get_skill_introduction', params)
  }
}
