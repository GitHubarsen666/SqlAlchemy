from marshmallow import Schema, fields

class PlainCinemaSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    location = fields.Str(required=True)

class PlainHallSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    capacity = fields.Int(required=True)
    cinema_id = fields.Int(load_only=True)

class PlainMovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    genre = fields.Str(required=True)
    duration = fields.Int(required=True)

class CinemaSchema(PlainCinemaSchema):
    halls = fields.List(fields.Nested(PlainHallSchema()), dump_only=True)

class HallSchema(PlainHallSchema):
    cinema_id = fields.Int(load_only=True)
    movies = fields.List(fields.Nested(PlainMovieSchema()), dump_only=True)

class MovieSchema(PlainMovieSchema):
    hall_id = fields.Int(load_only=True)