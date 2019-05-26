<template>
  <div id="whole">
    <div id="landing_box">
      <div class="login-frame">
      </div>
      <el-card class="login-window">
        <el-form :model="form_data" :rules="rules" ref="form">
          <el-form-item label="用户邮箱" prop="user_email">
            <el-input v-model="form_data.user_email"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input type="password" v-model="form_data.password"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onLogin('form')">登陆</el-button>
            <el-button @click="onRegister('form')">注册</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </div>
  </div>
</template>

<script>
import AuthApi from '@/apis/skill_learn_assistant/ordinary/AuthApi';
export default {
  name: 'OrdinaryAuth',
  data () {
    return {
      form_data: {
        user_email: '',
        password: ''
      },
      rules: {
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
    onLogin: function (form) {
      let that = this;
      this.$refs[form].validate((valid) => {
        if (valid) {
          let formData = new FormData();
          formData.append('user_email', that.form_data.user_email);
          formData.append('password', that.form_data.password);
          AuthApi.login(formData).then(function (result) {
            if (result.data.code === 1) {
              that.$store.dispatch('login');
              that.$router.replace('/skill_learn_assistant/');
            } else {
              alert(result.data.msg);
            }
          }).catch(function (error) {
            console.log(error);
          });
        }
      })
    },
    onRegister: function () {
      this.$router.push('/skill_learn_assistant/register')
    }
  }
}

</script>

<style scoped>
  #whole {
    height: 100%;
    width: 100%;
    opacity: 0.8;
    background: url('../../../assets/img/bg-6.png');
    background-size: cover;
  }
  #landing_box {
    width: 20%;
    height: 30%;
    position: absolute;
    top: 35%;
    left: 40%;
  }
  .login-frame {
    opacity: 0.3;
    height: 300px;
    width: 400px;
    position: absolute;
    top: 50%;
    left: 50%;
    border-radius: 10px;
    margin-top: -124px;
    margin-left: -204px;
    box-shadow: 10px 10px 1px #000000;
    animation: frame 2s linear;
  }
  .login-window {
    opacity: 0.9;
    height: 300px;
    width: 400px;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-top: -125px;
    margin-left: -205px;
    border: 1px solid #666;
    background: black;
    border-radius: 10px;
    animation: window 2s linear;
  }
  @keyframes window {
    0% {
      filter: alpha(opacity=0);
      opacity: 0;
      margin-top: -115px;
      margin-left: -195px;
    }
    70% {
      filter: alpha(opacity=0.5);
      opacity: 0.5;
      margin-top: -115px;
      margin-left: -195px;
    }
    100% {
      filter: alpha(opacity=0.7);
      margin-top: -125px;
      margin-left: -205px;
      opacity: 0.7;
    }
  }
  @keyframes frame {
    0% {
      filter: alpha(opacity=0);
      opacity: 0;
    }
    70% {
      filter: alpha(opacity=0);
      opacity: 0;
    }
    100% {
      filter: alpha(opacity=0.3);
      opacity: 0.3;
    }
  }
</style>
