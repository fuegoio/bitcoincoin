<template>
  <div>
    <v-row>
      <ProfileContainer />
    </v-row>
    <v-row>
      <WalletContainer />
    </v-row>
  </div>
</template>

<script>
import ProfileContainer from '@/containers/ProfileContainer'
import WalletContainer from '@/containers/WalletContainer'

export default {
  name: 'ProfilePage',
  components: {
    WalletContainer,
    ProfileContainer,
  },
}
</script>

<style scoped></style>
