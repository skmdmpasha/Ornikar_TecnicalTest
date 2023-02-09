import trafaret as t

# """
# Validation and parsing library.
# Trafaret is rigid and powerful lib to work with foreign data, configs etc.
# It provides simple way to check anything, and convert it accordingly to your needs.
# """

# # Below are objects used for validating response in api_employees.feature

empSchema = t.Dict({
    t.Key('status'): t.String,
    t.Key('data'): t.List(t.Dict({
        t.Key('id'): t.Int,
        t.Key('name'): t.String,
        t.Key('employee_name'): t.String,
        t.Key('employee_salary'): t.Int,
        t.Key('employee_age'): t.Int,
        t.Key('profile_image'): t.String
    })),
    # t.Key('required'): ["data"],
    t.Key('message'): t.String(allow_blank=True)
})

# empData = t.Dict({
#     t.Key('id'): t.Int,
#     t.Key('name'): t.String,
#     t.Key('employee_name'): t.String,
#     t.Key('employee_salary'): t.String,
#     t.Key('employee_age'): t.Int,
#     t.Key('profile_image'): t.String
# })

# twitterStatusEntitiesData = t.Dict({
#     t.Key('hashtags'): t.List(twitterHashtagEntity)
# })

# twitterHashtagEntity = t.Dict({
#     t.Key('text'): t.String,
#     t.Key('indices'): t.List(t.Int)
# })
