<template>
    <b-container id="search-wrapper">
        <b-row>
            <div class="input-group mb-3">
                <b-form-input
                    v-model="query"
                    type="text"
                    class="form-control"
                    placeholder="Introduce Twitter Username/Bio"
                    aria-label="Introduce Twitter Username/Bio"
                    aria-describedby="button-addon2"
                />
                <div class="input-group-append">
                    <b-form-select v-model="selected" :options="options"></b-form-select>
                    <b-button v-if="selected" @click="getProfiles(currentPage)" variant="outline-primary" :disabled="query == ''">Search!</b-button>
                    <b-button v-else @click="getTweets(currentPage)" variant="outline-primary" :disabled="query == ''">Search!</b-button>
                </div>
            </div>
        </b-row>
        <card :profiles="this.profiles"></card>
        <div class="overflow-auto" v-if="this.profiles !== null">
            <div class="mt-3">
                <b-pagination v-if="selected"
                    @input="getProfiles(currentPage)"
                    v-model="currentPage"
                    :total-rows="rows"
                    :per-page="perPage"
                    align="fill"
                ></b-pagination>
                <b-pagination v-else
                    @input="getTweets(currentPage)"
                    v-model="currentPage"
                    :total-rows="rows"
                    :per-page="perPage"
                    align="fill"
                ></b-pagination>
            </div>
        </div>
    </b-container>
</template>

<script>
import axios from 'axios';
import Card from './CardComponent';
export default {
    name: 'search',
    components: {
        Card
    },
    data() {
        return {
            selected: true,
            options: [
                { value: true, text: 'Search by username / bio' },
                { value: false, text: 'Search by tweet content' }
            ],
            query: '',
            rows: 900,
            perPage: 20,
            currentPage: 1,
            profiles: null
        };
    },
    methods: {
        getProfiles(currentPage) {
            // TODO: Fix this
            if (!Number.isInteger(currentPage)) {
                currentPage = 1;
            }
            const path = `http://localhost:5000/api/1.0/profiles/${this.query}/${this.perPage}/${currentPage}`;
            axios
                .get(path)
                .then(res => {
                    console.log(res.data);
                    this.profiles = res.data;
                })
                .catch(error => {
                    console.error(error);
                });
        },
        getTweets(currentPage){
            // TODO: Fix this
            if (!Number.isInteger(currentPage)) {
                currentPage = 1;
            }
            const path = `http://localhost:5000/api/1.0/search/${this.query}`;
            axios
                .get(path)
                .then(res => {
                    console.log(res.data.statuses);
                    let statuses = [];
                    res.data.statuses.forEach(status => {
                        status.user.tweet = status.text
                        statuses.push(status.user)
                    });
                    this.profiles = statuses;
                })
                .catch(error => {
                    console.error(error);
                });
        }
    }
};
</script>

<style>
#search-wrapper {
    margin-top: 50px;
}
</style>
