<template>
  <v-row>
    <v-col :cols="12">
      <ProfileCard :user="user" />
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import ProfileCard from '@/components/profiles/ProfileCard.vue'

import auth from '../modules/auth'

@Component({
  components: {
    ProfileCard,
  },
})
export default class ProfileContainer extends Vue {
  user = {
    username: auth.user.profile.username,
    cashFlow: 1000000,
    joinDate: '5 weeks ago',
  }
}
</script>

<style scoped></style>
