<template>
  <v-row>
    <v-col :cols="5">
      <ProfileCard />
    </v-col>
  </v-row>
</template>

<script>
import ProfileCard from '@/components/profiles/ProfileCard'
export default {
  name: 'ProfileContainer.vue',
  components: { ProfileCard },
}
</script>

<style scoped></style>
