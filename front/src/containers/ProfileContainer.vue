<template>
  <v-row>
    <v-col :cols="12">
      <ProfileCard v-bind:user="user" />
    </v-col>
  </v-row>
</template>

<script>
import ProfileCard from '@/components/profiles/ProfileCard'
export default {
  name: 'ProfileContainer.vue',
  components: { ProfileCard },
  data: function() {
    return {
      user: {
        username: 'Quentin Churet',
        cashFlow: 1000000,
        joinDate: '5 weeks ago',
      },
    }
  },
}
</script>

<style scoped></style>
