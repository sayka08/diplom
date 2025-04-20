<!-- frontend/src/views/Login.vue -->
<template>
  <div class="login-container d-flex flex-column flex-lg-row align-items-center justify-content-center">
    <div class="left-section text-center text-lg-start mb-4 mb-lg-0">
      <h1 class="facebook-title">aldik</h1>
      <p class="facebook-subtitle">
        Aldik помогает вам всегда оставаться на связи
        и общаться со своими знакомыми.
      </p>
    </div>
    <div class="right-section">
      <div class="card shadow-sm p-3 mb-3 bg-white rounded" style="width: 360px;">
        <h3 class="text-center mb-2">Вход на Aldik</h3>
        <form @submit.prevent="onSubmit">
          <div class="mb-3">
            <input
              type="text"
              class="form-control form-control-lg"
              placeholder="Имя пользователя"
              v-model="username"
            />
          </div>
          <div class="mb-3">
            <input
              type="password"
              class="form-control form-control-lg"
              placeholder="Пароль"
              v-model="password"
            />
          </div>
          <button type="submit" class="btn btn-primary btn-lg w-100">
            Вход
          </button>
        </form>
        <hr />
        <div class="text-center">
          <button
            class="btn btn-success btn-md mt-2"
            @click="goToRegister"
          >
            Создать новый аккаунт
          </button>
        </div>
      </div>
      <div v-if="successMessage" class="alert alert-success mt-3">
        {{ successMessage }}
      </div>
      <div v-if="errorMessage" class="alert alert-danger mt-3">
        {{ errorMessage }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: '',
      successMessage: '',
    };
  },
  methods: {
    async onSubmit() {
      this.errorMessage = '';
      this.successMessage = '';
      try {
        console.log('Sending login request:', {
          username: this.username,
          password: this.password,
        });
        const response = await this.$axios.post('/login', {
          username: this.username,
          password: this.password,
        });
        console.log('Login response:', response.data);
        localStorage.setItem('access_token', response.data.access_token);
        this.successMessage = 'Вход выполнен!';
        await new Promise(resolve => setTimeout(resolve, 500));
        this.$router.push('/posts');
      } catch (error) {
        this.errorMessage = error.response?.data?.detail || 'Login failed';
        console.error('Login error:', error.response?.data || error.message);
      }
    },
    goToRegister() {
      this.$router.push('/register');
    },
  },
};
</script>

<style scoped>
.login-container {
  min-height: 100vh;
  padding: 1rem;
  background-color: #f0f2f5;
}
.left-section {
  max-width: 600px;
  margin-right: 2rem;
}
.facebook-title {
  font-size: 3.5rem;
  color: #1877f2;
  font-weight: bold;
  font-family: Helvetica, Arial, sans-serif;
}
.facebook-subtitle {
  font-size: 1.2rem;
  color: #1c1e21;
  font-family: Helvetica, Arial, sans-serif;
}
.right-section {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.card {
  border: none;
}
.form-control-lg {
  font-size: 1rem;
  padding: 0.75rem 1rem;
}
.btn-lg {
  font-size: 1rem;
  padding: 0.75rem 1rem;
}
</style>