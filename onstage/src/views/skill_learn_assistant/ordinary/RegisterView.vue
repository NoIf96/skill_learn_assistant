<template>
  <div id="whole">
    <div id="landing_box">
      <el-card class="registration">
        <el-form :model="form_data" ref="form" :rules="rules">
          <el-form-item label="用户名" prop="user_name">
            <el-input v-model="form_data.user_name"></el-input>
          </el-form-item>
          <el-form-item label="用户邮箱" prop="user_email">
            <el-input v-model="form_data.user_email"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input type="password" v-model="form_data.password"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="register('form')">注册</el-button>
            <el-button @click="$router.go(-1)">返回</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </div>
  </div>
</template>

<script>
import AuthApi from '@/apis/skill_learn_assistant/ordinary/AuthApi';
export default {
  name: 'RegisterView',
  data () {
    return {
      form_data: {
        user_name: '',
        user_email: '',
        password: ''
      },
      rules: {
        user_name: [
          { required: true, message: '请输入用户名', trigger: 'blur' }
        ],
        user_email: [
          { required: true, message: '请输入邮箱地址', trigger: 'blur' },
          { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    register: function (form) {
      let that = this;
      this.$refs[form].validate((valid) => {
        if (valid) {
          let formData = new FormData();
          formData.append('user_name', that.form_data.user_name);
          formData.append('user_email', that.form_data.user_email);
          formData.append('password', that.form_data.password);
          AuthApi.register(formData).then(function (result) {
            if (result.data.code === 1) {
              that.$router.replace('/skill_learn_assistant/login');
            } else {
              alert(result.data.msg);
            }
          }).catch(function (error) {
            console.log(error);
          });
        }
      })
    }
  }
}
</script>

<style scoped>
  #whole {
    height: 100%;
    width: 100%;
    opacity: 0.8;
    background: url('../../../assets/img/bg-4.jpg');
    background-size: cover;
  }
  #landing_box {
    width: 20%;
    height: 30%;
    position: absolute;
    top: 25%;
    left: 40%;
  }
  .registration {
    opacity: 0.9;
    height: 390px;
    width: 400px;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-top: -125px;
    margin-left: -205px;
    border: 1px solid #666;
    background: black;
    border-radius: 10px;
  }
</style>
