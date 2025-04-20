<!-- frontend/src/views/Register.vue -->
<template>
  <div class="register-container d-flex flex-column align-items-center justify-content-center">
    <h1 class="facebook-title">aldik</h1>
    <div class="card register-card shadow p-3 mb-3 bg-white rounded">
      <h3 class="text-center mb-2">Создайте новый аккаунт</h3>
      <p class="text-center mb-4">Это быстро и просто.</p>
      <form @submit.prevent="onSubmit">
        <div class="mb-3">
          <input
            type="text"
            class="form-control"
            placeholder="Имя пользователя"
            v-model="username"
          />
        </div>
        <div class="mb-3">
          <input
            type="password"
            class="form-control"
            placeholder="Пароль"
            v-model="password"
          />
        </div>
        <button type="submit" class="btn btn-success w-100">
          Зарегистрироваться
        </button>
      </form>
      <div class="mt-3 text-center">
        <a href="#" @click.prevent="goToLogin" class="link-secondary">
          У вас уже есть аккаунт?
        </a>
      </div>
    </div>
    <div v-if="successMessage" class="alert alert-success mt-3">
      {{ successMessage }}
    </div>
    <div v-if="errorMessage" class="alert alert-danger mt-3">
      {{ errorMessage }}
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      successMessage: '',
      errorMessage: '',
    };
  },
  methods: {
    async onSubmit() {
      this.successMessage = '';
      this.errorMessage = '';
      try {
        console.log('Sending register request:', {
          username: this.username,
          password: this.password,
        });
        const response = await this.$axios.post('/register', {
          username: this.username,
          password: this.password,
        });
        console.log('Register response:', response.data);
        this.successMessage = `Успешно зарегистрированы: ${response.data.username}`;
        await new Promise(resolve => setTimeout(resolve, 500));
        this.$router.push('/login');
      } catch (error) {
        this.errorMessage = error.response?.data?.detail || 'Registration failed';
        console.error('Register error:', error.response?.data || error.message);
      }
    },
    goToLogin() {
      this.$router.push('/login');
    },
  },
};
</script>

<style scoped>
.register-container {
  min-height: 100vh;
  background-color: #f0f2f5;
  padding: 2rem;
}
.facebook-title {
  font-size: 3.5rem;
  color: #1877f2;
  font-weight: bold;
  font-family: Helvetica, Arial, sans-serif;
  margin-bottom: 1rem;
}
.register-card {
  width: 400px;
  max-width: 90%;
}
.link-secondary {
  text-decoration: none;
  color: #606770;
}
.link-secondary:hover {
  text-decoration: underline;
}
</style>