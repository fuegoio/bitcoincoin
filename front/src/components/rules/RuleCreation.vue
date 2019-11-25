<template>
  <div class="rule-creation elevation-0">
    <v-toolbar color="primary" dark flat>
      <template v-slot:extension>
        <v-toolbar-title class="font-weight-bold headline pl-2">
          Création d'une nouvelle règle pour le Paracétamol
        </v-toolbar-title>
        <v-btn color="accent" dark absolute bottom right fab>
          <v-icon>mdi-plus</v-icon>
        </v-btn>
      </template>
    </v-toolbar>
    <v-row class="mx-6 mt-10">
      <v-col cols="7">
        <v-text-field
          v-model="ruleName"
          label="Nom de la règle"
          outlined
          hide-details
          placeholder="Posologie maximale pour les personnes agées de 3g/jour"
        ></v-text-field>
      </v-col>
      <v-col cols="3">
        <v-select
          v-model="ruleType"
          :items="ruleTypeDefinitions"
          label="Type de règle"
          outlined
          item-value="key"
          hide-details
        >
          <template v-slot:item="{ item }">
            <v-icon small class="mr-4">{{ item.icon }}</v-icon>
            {{ item.label }}
          </template>
          <template v-slot:selection="{ item }">
            <v-icon small class="mx-3 mt-1">{{ item.icon }}</v-icon>
            <span class="font-weight-bold mt-1 title">{{ item.label }}</span>
          </template>
        </v-select>
      </v-col>
      <v-col cols="2">
        <v-select
          v-model="ruleGravity"
          :items="ruleGravityDefinitions"
          label="Gravité"
          outlined
          item-text="label"
          item-value="key"
          hide-details
        ></v-select>
      </v-col>
      <v-col cols="12">
        <v-textarea
          label="Description de la règle"
          outlined
          hide-details
          placeholder="Décrivez dans quel cas cette règle s'applique et l'intervention associée ..."
        ></v-textarea>
      </v-col>
      <v-col cols="12">
        <v-divider></v-divider>
      </v-col>
      <v-col cols="12" class="mt-4">
        <v-expand-transition>
          <OverdoseDetailsTemplate v-if="ruleType === 'OVERDOSE'" />
        </v-expand-transition>
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import OverdoseDetailsTemplate from '@/components/details/templates/OverdoseDetailsTemplate.vue'
import {
  Rule,
  RuleTypeDefinition,
  RuleTypeDefinitions,
  RuleGravityDefinition,
  RuleGravityDefinitions,
} from '@/models/rules'

@Component({
  components: {
    OverdoseDetailsTemplate,
  },
})
export default class RulesDetails extends Vue {
  public rule!: Rule
  public ruleName = ''
  public ruleType = RuleTypeDefinitions[0].key
  public ruleGravity = RuleGravityDefinitions[0].key

  public get ruleTypeDefinitions(): RuleTypeDefinition[] {
    return RuleTypeDefinitions
  }

  public get ruleGravityDefinitions(): RuleGravityDefinition[] {
    return RuleGravityDefinitions
  }
}
</script>

<style lang="scss" scoped>
@import '~vuetify/src/styles/styles';

.medical-problems {
  border-style: solid;
  border-radius: 4px;
  border-width: thin;
  border-color: map-get($material-light, 'dividers') !important;
  border-bottom-width: 0;

  > .medical-problems--btn.medical-problems--btn {
    border-bottom-width: 1px;
    border-color: map-get($material-light, 'dividers') !important;
  }
}
</style>
